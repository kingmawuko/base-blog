from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PostModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug= models.SlugField(default=True)
    # ratings 
    #image = models.ImageField(upload_to='images', null=True)
  
    

    def __str__(self):
        return self.title


# should be able to edit/delete post 
# next time name it as CommentModel
class Comment(models.Model):
    post=models.ForeignKey(PostModel,related_name='comment',on_delete=models.CASCADE,default=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True)
    date_added=models.DateTimeField(auto_now=True)


    like =None # all three need a foreignkey
    dislike =None
    reply_comment = None


# the person 
class Account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # profile picture 
    # username-email

    
