from django.urls import path
from django.contrib.auth import views
from .views import index, category, contact, signup
from .forms import LoginForm

app_name = "core"

urlpatterns = [
  path("", index, name="index"),
  path("category/<int:pk>/", category, name="category"),
  path("contact/", contact, name="contact"),
  path("signup/", signup, name="signup"),
  path("login/", views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login"),
]