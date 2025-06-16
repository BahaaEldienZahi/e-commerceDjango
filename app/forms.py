from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Product



# User registration form

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Product Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Price', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=None, label='Category', widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Category  # Import Category model here to avoid circular import
        self.fields['category'].queryset = Category.objects.all()       
    class Meta:
        model = User
        fields = ['name', 'price', 'category']    
        
class HomeForm(forms.Form):
    name = forms.CharField(max_length=100, label='Home Name', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['name']       

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' 
        
