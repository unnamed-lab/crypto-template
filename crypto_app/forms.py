from django import forms

from crypto_app.models import UserPaymentReview

class UserPaymentForm(forms.ModelForm):
    user = forms.EmailField(initial='Default Value',widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control",'readonly': 'readonly'}))
    title = forms.CharField(initial='Default Value',widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control",'readonly': 'readonly'}))
    initial = forms.CharField(initial='Default Value',widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control",'readonly': 'readonly'}))
    invested_amount = forms.CharField(initial='Default Value',widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control",'readonly': 'readonly'}))
    invested_return = forms.CharField(initial='Default Value', widget=forms.TextInput(attrs={"placeholder": "", "class": "form-control",'readonly': 'readonly'}))
    
    class Meta:
        model = UserPaymentReview
        fields = ['title','initial','invested_amount','invested_return']

