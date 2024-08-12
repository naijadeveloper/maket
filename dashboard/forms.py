from django import forms
from .models import Profile, UserRating

CSS_CLASSES = "peer appearance-none px-2 py-2 bg-neutral-700 text-neutral-300 font-semibold rounded outline-none border-4 border-transparent border-b-neutral-600 focus:border-neutral-600"


class UserRatingForm(forms.ModelForm):
  class Meta:
    model = UserRating
    fields = ("rate", "description")
    widgets = {
      "rate": forms.NumberInput(attrs={
        "class": "w-[90px] appearance-none px-2 py-2 bg-neutral-700 text-neutral-300 font-semibold rounded outline-none border-4 border-transparent border-b-neutral-600 focus:border-neutral-600",
        "placeholder": "1 - 5",
        "min": "1",
        "max": "5"
      }),

      "description": forms.Textarea(attrs={
        "class": "w-full appearance-none px-2 py-2 bg-neutral-700 text-neutral-300 font-semibold rounded outline-none border-4 border-transparent border-b-neutral-600 focus:border-neutral-600",
        "placeholder": "Reason for your rating",
        "rows": "5"
      })
    }



class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ("profile_image", "allow_banner", "profile_banner", "banner_number", "bio", "country", "state", "city")
    widgets = {
      "profile_image": forms.FileInput(attrs={
        "class": CSS_CLASSES
      }),

      "allow_banner": forms.CheckboxInput(attrs={
        "class": "ml-1 mt-2"
      }),

      "profile_banner": forms.FileInput(attrs={
        "class": CSS_CLASSES
      }),

      "banner_number": forms.NumberInput(attrs={
        "class": CSS_CLASSES,
        "min": "1",
        "max": "4"
      }),

      "bio": forms.Textarea(attrs={
        "class": f"{CSS_CLASSES} [&::-webkit-scrollbar]:w-2 [&::-webkit-scrollbar]:h-2 [&::-webkit-scrollbar-track]:bg-neutral-700 [&::-webkit-scrollbar-track]:rounded-r [&::-webkit-scrollbar-thumb]:bg-neutral-300",
        "rows": "5"
      }),

      "country": forms.TextInput(attrs={
        "class": CSS_CLASSES
      }),

      "state": forms.TextInput(attrs={
        "class": CSS_CLASSES
      }),

      "city": forms.TextInput(attrs={
        "class": CSS_CLASSES
      }),
    }