from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from .countries import sorted_countries
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username","class": "form-field"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-field"}))
    address = forms.ChoiceField(choices=sorted_countries, widget=forms.Select(attrs={"placeholder": "Country", "class": "form-field"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-field"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password", "class": "form-field"}))
    
    class Meta:
        model = User
        fields = ['username','email','address']
        


