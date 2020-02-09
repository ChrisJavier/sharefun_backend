from django import forms
from mygroup.models import Post


class ListForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [""]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
