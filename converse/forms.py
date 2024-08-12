from django import forms

from .models import ConverseMessage

class ConverseMessageForm(forms.ModelForm):
  class Meta:
    model = ConverseMessage
    fields = ("content",)
    widgets = {
      "content": forms.Textarea(attrs={
        "class": "peer appearance-none px-2 py-2 bg-neutral-700 text-neutral-300 font-semibold rounded outline-none border-4 border-transparent border-b-neutral-600 focus:border-neutral-600",
        "placeholder": "Type in here the message you want to send"
      })
    }