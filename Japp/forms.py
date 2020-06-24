from django import forms
from django.forms import ModelForm
from .models import Customer, Order

#create your forms


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'name',
            'phone',
            'email'
        ]
        labels = {
            'name': 'name',
            'phone': 'phone',
            'email': 'email'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Please enter your name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Please enter your phone number'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Please enter your email'
            })
        }



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['time_created']