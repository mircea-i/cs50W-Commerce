from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("view_listing/<int:id>", views.view_listing, name="view_listing"),
    path("end_listing/<int:id>", views.end_listing, name="end_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist_add/<int:id>", views.watchlist_add, name="watchlist_add"),
    path("watchlist_remove/<int:id>", views.watchlist_remove, name="watchlist_remove"),
    path("post_comment/<int:id>", views.post_comment, name="post_comment"),
    path("bid/<int:id>", views.bid, name="bid"),
    path("categories", views.categories, name="categories")
]
