from django import forms
from . models import PostModel




class PostForm(forms.ModelForm):
    email =forms.EmailField()


    class Meta:
        model=PostModel
        fields=['title','description']