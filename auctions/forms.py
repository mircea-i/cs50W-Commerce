from django.forms import ModelForm, Form
from django import forms
from .models import Listing
# Create listing form
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'description', 'category', 'image', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }

