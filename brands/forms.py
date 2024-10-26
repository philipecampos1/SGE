from django import forms
from . import models


class BrandForm(forms.ModelForm):

    class Meta:
        model = models.Brands
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
        labels = {
            'name': 'Name',
            'description': 'Description'
        }
