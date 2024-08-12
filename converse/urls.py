from django.urls import path
from .views import new_converse, inbox, detail

app_name = "converse"

urlpatterns = [
  path("", inbox, name="inbox"),
  path("<int:pk>/", detail, name="detail"),
  path("new/<int:item_pk>/", new_converse, name="new")
]