from django import forms
from .models import Customer
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password


class CustomersignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class meta:
        model = Customer
        fields = ['username', 'email', 'first_name', 'last_name', 'address', 'phone_number', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        # Hash the password before saving
        cleaned_data['password'] = make_password(password)
        return cleaned_data
    
class CustomerloginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))