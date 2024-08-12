from django.urls import path
from .views import browse, detail, reviews, newItem, editItem, delete

app_name = "item"

urlpatterns = [
  path("browse/", browse, name="browse"),
  path("new-item/", newItem, name="newItem"),
  path("<int:pk>/", detail, name="detail"),
  path("<int:pk>/reviews/", reviews, name="reviews"),
  path("<int:pk>/edit/", editItem, name="edit"),
  path("<int:pk>/delete/", delete, name="delete"),
  path("<int:pk>/<str:cart>", detail, name="detail"),
]