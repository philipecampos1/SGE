from django import forms
from . import models


class InflowForm(forms.ModelForm):

    class Meta:
        model = models.Inflows
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
        labels = {
            'supplier': 'Supplier',
            'procuct': 'Product',
            'quantity': 'Quantity',
            'description': 'Description'
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError('Must be greater than zero')
        return quantity
