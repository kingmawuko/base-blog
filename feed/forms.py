from django import forms
from . models import PostModel,CommentModel



# the post will always be made from the admin page 
class PostForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=['title','description']

class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentModel 
        fields=['comment']
      