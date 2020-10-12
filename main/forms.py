from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "Username"})
        self.fields['email'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "email"})
        self.fields['first_name'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "first name"})
        self.fields['last_name'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "last name"})
        self.fields['password1'].widget.attrs.update({'class': 'input100' ,'placeholder': "password"})
        self.fields['password2'].widget.attrs.update({'class': 'input100' , 'placeholder':"confirm password"})
   
    class Meta:
        model = User
        fields = ['username' , 'password1' , 'password2' , 'email' , 'first_name' , 'last_name']


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "phone"})
        self.fields['twitter'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "twitter"})
        self.fields['instagram'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "instagram"})
        self.fields['facebook'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "facebook"})
        self.fields['image'].widget.attrs.update({'class': 'input100' , 'id':"exampleFormControlTextarea1" , 'rows' : "5" , 'placeholder': "image"})

    class Meta:
        model= models.Customer
        fields = '__all__'
        exclude = ['user']


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': "E-mail"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "message"}))
