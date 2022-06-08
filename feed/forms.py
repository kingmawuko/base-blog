from django import forms
from . models import PostModel,Comment



# the post will always be made from the admin page 
class PostForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=['title','description']




class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']
        widgets = {'comments':forms.TextInput(attrs={'class':'form-control'}),}