from django.db import models
from django.contrib.auth.models import User
from dashboard.helper import validate_range

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255, unique=True)
  description = models.TextField(default="")

  class Meta:
    ordering = ('name',)
    verbose_name_plural = "Categories"

  def __str__(self):
    return self.name


class Item(models.Model):
  category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  price = models.FloatField()
  image = models.ImageField(upload_to="item_images", blank=True, null=True)
  stock = models.IntegerField(default=1)
  is_sold = models.BooleanField(default=False)
  created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ("-created_at",)

  def __str__(self):
    return f"{self.created_by.username} :: {self.name}"



class ItemRating(models.Model):
  created_by = models.ForeignKey(User, related_name="item_ratings", on_delete=models.CASCADE)
  rated_item = models.ForeignKey(Item, related_name="item_ratings", on_delete=models.CASCADE)
  rate = models.IntegerField(validators=[validate_range])
  description = models.TextField(default="")
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.created_by.username} ::{self.rated_item.created_by}'s {self.rated_item.name} ::{self.rate}"
