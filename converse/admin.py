from django.contrib import admin
from .models import Converse, ConverseMessage

# Register your models here.
admin.site.register(Converse)
admin.site.register(ConverseMessage)