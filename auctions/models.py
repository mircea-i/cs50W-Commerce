from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, MinValueValidator

class User(AbstractUser):
    pass
    def __str__(self):
        return self.username

class Listing(models.Model):
    name = models.CharField(max_length=64, validators=[MinLengthValidator(1)])
    description = models.TextField(max_length=1024, validators=[MinLengthValidator(1)])
    creation = models.DateTimeField(default=timezone.now())
    image = models.URLField(max_length=200, blank=True)
    starting_bid = models.FloatField(validators=[MinValueValidator(1)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name} at {self.starting_bid} by {self.owner}"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.FloatField(validators=[MinValueValidator(1)])


class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.author} commented: {self.comment}"

class Watchlist(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.listing} watched by {self.user}"