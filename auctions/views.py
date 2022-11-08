from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from .models import User, Listing, Bid, Comment, Watchlist, Category
from .forms import ListingForm


def index(request):
    return render(request, "auctions/index.html", {
        'listings': Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return redirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create(request):

    # If form submitted then create a form from post data
    if request.method == "POST":
        form = ListingForm(request.POST)

        # Check form data, combine it with current datetime and user and save the object to db
        if form.is_valid():
            Listing.objects.create(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                category = form.cleaned_data['category'],
                creation = timezone.now(),
                image = form.cleaned_data['image'],
                price = form.cleaned_data['price'],
                owner = request.user,
                is_active = "True"
                )

            # Go back to index
            return redirect(reverse("index"))

    # Create blank form and present it to the user
    else:
        return render(request, "auctions/create.html", {'form':ListingForm()}) 


def view_listing(request, id):

    # Get the listing for the current id
    listing = Listing.objects.get(pk=id)

    # Do all the magic if the user is not Anonymous
    if request.user.is_authenticated:
        
        # Get the current user and the comments for the listing
        user = request.user
        comments = Comment.objects.filter(listing=listing)
        

        # Check if current listing is being watched by the logged in user in order to pass it to the template
        watched = False
        if Watchlist.objects.filter(listing=listing, user=request.user):
            watched = True

        # Check if current listing has ended and user is highest bidder
        won = False
        if listing.is_active != True and Bid.objects.filter(listing=listing, bidder=request.user):
            won = True
        
        # Render the template with all the information
        return render(request, "auctions/view_listing.html", {
            'name': listing.name,
            'owner': listing.owner,
            'creation': listing.creation,
            'description': listing.description,
            'image': listing.image,
            'is_active': listing.is_active,
            'id': id,
            'user': user,
            'comments': comments,
            'watched': watched,
            'won': won,
            'bid': listing.price
        })

    # If the user is not logged in
    else:

        # Return the template with limited information
        return render(request, "auctions/view_listing.html", {
            'name': listing.name,
            'owner': listing.owner,
            'creation': listing.creation,
            'description': listing.description,
            'image': listing.image,
            'id': id,
            'bid': listing.price
        })


@login_required
def watchlist(request):

    # Query active listings against the current user's watchlist
    watchlist = Listing.objects.filter(is_active=True, id__in=(Watchlist.objects.filter(user=request.user).values_list('listing')))

    return render(request, "auctions/watchlist.html", {'listings': watchlist})


@login_required
def end_listing(request, id):

    # Getting here via form submit
    if request.method == "POST":
        listing = Listing.objects.get(pk=id)

        # Make the listing inactive
        listing.is_active = False
        listing.save()

        # Go back to auctions list
        return view_listing(request, id)
    
    # If feeling funky redirect back to auctions list
    else:
        return redirect(reverse("index"))


@login_required
def post_comment(request, id):
    
    # Getting here via comment form submit
    if request.method == "POST":
        listing = Listing.objects.get(pk=id)

        # Create new comment object if comment exists
        if request.POST['comment'] != "":
            Comment.objects.create(
                    listing = listing,
                    comment = request.POST['comment'],
                    author = request.user
                    )
        
        # Render the same listing adding the new comment
        return view_listing(request, id)

    # If feeling funky redirect back to auctions list
    else:
        return redirect(reverse("index"))

@login_required
def watchlist_add(request, id):

    # Add current viewed listing to watchlist
    if request.method == "POST":
        listing = Listing.objects.get(pk=id)
        Watchlist.objects.create(listing=listing, user=request.user)
        return view_listing(request, id)
    
    # If feeling funky redirect back to auctions list
    else:
        return redirect(reverse("index"))


@login_required
def watchlist_remove(request, id):

    # Remove currently viewed item from watchlist
    if request.method == "POST":
        listing = Listing.objects.get(pk=id)
        Watchlist.objects.filter(listing=listing, user=request.user).delete()
        return view_listing(request, id)
    # If feeling funky redirect back to auctions list
    else:
        return redirect(reverse("index"))


@login_required
def bid(request, id):

    # Get the listing object and the posted bid
    if request.method == "POST":
        listing = Listing.objects.get(pk=id)
        posted_bid = request.POST['bid']

        # Check if bid value is numeric
        try:
            posted_bid = float(posted_bid)
        except ValueError:
            return render(request, "auctions/error.html", {'error': 'Invalid bid, please place a valid bid!'})

        # Check if bid value is higher than
        if posted_bid <= listing.price:
            return render(request, "auctions/error.html", {'error': 'Bid value too low, please place a higher bid!'})
        else:
            Bid.objects.update_or_create(
                listing = listing,
                bidder = request.user
            )
            listing.price = posted_bid
            listing.save()
            return view_listing(request, id)



def categories(request):
    return render(request, "auctions/categories.html", {
        'categories': Category.objects.all()})

def category(request, name):
    return render(request, "auctions/category.html", {
        'listings': Listing.objects.filter(category=Category.objects.get(name=name)),
        'category':name
    })
