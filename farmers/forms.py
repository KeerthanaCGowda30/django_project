from django import forms
from .models.farmers import Farmer
from .models.products import Product

class FarmerProfileForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['image','name' ,'email','phone', 'location']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']
        
