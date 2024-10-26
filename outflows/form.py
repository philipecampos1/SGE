from django import forms
from . import models
from django.core.exceptions import ValidationError


class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
        labels = {
            'procuct': 'Product',
            'quantity': 'Quantity',
            'description': 'Description'
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'Quantity availible for the product {product.title} is {product.quantity} '
            )
        return quantity
