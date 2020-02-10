from django import forms
from mypost.models import Post, Customer, DriverUser


class ListForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [""]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)


class ProfileDetails(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = [""]


class UserForm(forms.ModelForm):
    class Meta:
        model = DriverUser
        exclude = [""]

