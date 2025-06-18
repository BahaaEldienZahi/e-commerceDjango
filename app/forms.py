from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Product , Category



# User registration form

class ProductForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'details', 'img', 'category']  
        
class HomeForm(forms.Form):
    name = forms.CharField(max_length=100, label='Home Name', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['name']       

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__' 
        
