from django.forms import ModelForm, Form
from django import forms
from .models import Listing

# Create listing form
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'description', 'image', 'starting_bid']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control'})
        }

