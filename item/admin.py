from django.contrib import admin
from .models import Category, Item, ItemRating

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemRating)
