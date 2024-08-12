from django.db import models
from django.contrib.auth.models import User
from item.models import Item
from .helper import validate_range, validate_range_banner

# Create your models here.
class UserRating(models.Model):
  created_by = models.ForeignKey(User, related_name="user_ratings", on_delete=models.CASCADE)
  rated_user = models.ForeignKey(User, related_name="user_rated", on_delete=models.CASCADE)
  rate = models.IntegerField(validators=[validate_range])
  description = models.TextField(default="")
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.created_by.username}::{self.rated_user.username}::{self.rate}"


class Cart(models.Model):
  created_by = models.ForeignKey(User, related_name="carts", on_delete=models.CASCADE)
  item = models.ForeignKey(Item, related_name="carts", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.created_by.username}::{self.item.name}"


class Profile(models.Model):
  created_by = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
  bio = models.TextField(default="")
  country = models.CharField(max_length=255, blank=True)
  state = models.CharField(max_length=255, blank=True)
  city = models.CharField(max_length=255, blank=True)
  allow_banner = models.BooleanField(default=True)
  banner_number = models.IntegerField(default=1, validators=[validate_range_banner])
  profile_banner = models.ImageField(upload_to="profile_banners", blank=True, null=True)
  profile_image = models.ImageField(upload_to="profile_images", blank=True, null=True)

  def __str__(self):
    return self.created_by.username