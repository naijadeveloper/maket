from django.contrib import admin
from .models import UserRating, Cart, Profile

# Register your models here.
admin.site.register(UserRating)
admin.site.register(Cart)
admin.site.register(Profile)