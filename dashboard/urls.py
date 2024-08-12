from django.urls import path
from .views import index, profile, settings, categories, cart, logout_user


app_name = "dashboard"

urlpatterns = [
  path("", index, name="index"),
  path("profile/", profile, name="profile"),
  path("settings/", settings, name="settings"),
  path("category/", categories, name="category"),
  path("cart/", cart, name="cart"),
  path("cart/remove/<int:cart_id>/", cart, name="cart"),
  path("logout/", logout_user, name="logout"),
  path("<str:username>/", profile, name="other_user_profile"),
]