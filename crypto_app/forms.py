from django import forms

from crypto_app.models import UserPaymentReview

class UserPaymentForm(forms.ModelForm):
    user = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control","disabled":True,"required":False}))
    title = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control","disabled":True,"required":False}))
    initial = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control","disabled":True,"required":False}))
    invested_amount = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control","disabled":True,"required":False}))
    invested_return = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control","disabled":True,"required":False}))
    
    class Meta:
        model = UserPaymentReview
        fields = ['title','initial','invested_amount','invested_return']

