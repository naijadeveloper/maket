from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


CSS_CLASSES = "peer appearance-none px-2 py-2 bg-neutral-700 text-neutral-300 font-semibold rounded outline-none border-4 border-transparent border-b-neutral-600 focus:border-neutral-600"

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={
    "placeholder": "",
    "class": CSS_CLASSES
  }))

  password = forms.CharField(widget=forms.PasswordInput(attrs={
    "placeholder": "",
    "class": CSS_CLASSES
  }))


class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")

  username = forms.CharField(widget=forms.TextInput(attrs={
    "class": CSS_CLASSES
  }))

  email = forms.CharField(widget=forms.EmailInput(attrs={
    "class": CSS_CLASSES
  }))

  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    "class": CSS_CLASSES
  }))

  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    "class": CSS_CLASSES
  }))