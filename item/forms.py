from django import forms
from .models import Item, ItemRating

CSS_CLASSES = "peer appearance-none px-2 py-2 bg-neutral-700 text-neutral-300 font-semibold rounded outline-none border-4 border-transparent border-b-neutral-600 focus:border-neutral-600"

class NewItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ("category", "name", "description", "price", "stock", "image",)

    widgets = {
      "category": forms.Select(attrs={
        "class": CSS_CLASSES
      }),

      "name": forms.TextInput(attrs={
        "class": CSS_CLASSES
      }),

      "description": forms.Textarea(attrs={
        "class": CSS_CLASSES
      }),

      "price": forms.NumberInput(attrs={
        "class": CSS_CLASSES,
        "min": "10"
      }),

      "stock": forms.NumberInput(attrs={
        "class": CSS_CLASSES,
        "min": "1"
      }),

      "image": forms.FileInput(attrs={
        "class": CSS_CLASSES
      })
    }


class EditItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ("name", "description", "price", "image", "stock", "is_sold")
    widgets = {
      "name": forms.TextInput(attrs={
        "class": CSS_CLASSES
      }),

      "description": forms.Textarea(attrs={
        "class": f"{CSS_CLASSES} [&::-webkit-scrollbar]:w-2 [&::-webkit-scrollbar]:h-2 [&::-webkit-scrollbar-track]:bg-neutral-700 [&::-webkit-scrollbar-track]:rounded-r [&::-webkit-scrollbar-thumb]:bg-neutral-300",
        "rows": "5"
      }),

      "price": forms.NumberInput(attrs={
        "class": CSS_CLASSES,
        "min": "10"
      }),

      "stock": forms.NumberInput(attrs={
        "class": CSS_CLASSES,
        "min": "1"
      }),

      "is_sold": forms.CheckboxInput(attrs={
        "class": CSS_CLASSES,
      }),

      "image": forms.FileInput(attrs={
        "class": CSS_CLASSES
      })
    }



class ItemRatingForm(forms.ModelForm):
  class Meta:
    model = ItemRating
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