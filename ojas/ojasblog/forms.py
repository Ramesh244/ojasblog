from tkinter import Widget
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ContactForm,Bhagavan


class SigninForm(UserCreationForm):
     password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
     phone_number=forms.IntegerField()
     age=forms.IntegerField()
     class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        

class EditDashboad(forms.ModelForm):
  class Meta:
    model = Bhagavan
    fields ='__all__'
    Widgets={'paragram':forms.Textarea()}

class EditAdminDashborad(UserChangeForm):
  password = None
  class Meta:
    model = User
    fields = '__all__'
    labels = {'email': 'Email'}

class Contact(forms.ModelForm):
  class Meta:
    model = ContactForm
    fields = '__all__'



