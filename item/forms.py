from django import forms
from .models import Item

class NewItemFor(forms.ModelForm):
    class Meta:
        model = Item
        fields=('category','name','decription','price','image')