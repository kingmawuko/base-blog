from django.db import models
from django.contrib.auth.models import User




class PostModel(models.Model):
    # Postmodel_title 
    title = models.CharField(max_length=50)
    description = models.TextField()
    # remove this 
     # this is pointless / it should be a star rating iver 
    favourites = models.ManyToManyField(User,related_name='favourite',default=None,blank=True)     
  
    def __str__(self):
        return self.title


    @property
    # Postmodel_num_likes 
    def num_likes(self):
        return self.liked.all.count()
LIKE_CHOICES = (

    ('like', 'like'),
    ('unlike','unlike')
)


# like_model / this is pointless 
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default="Like" , max_length=10)

    def __str__(self) :
        return str(self.post)


# comment_model 
class CommentModel(models.Model): 
    post=models.ForeignKey(PostModel,related_name='comment',on_delete=models.CASCADE,default=True)      
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True)
    date_added=models.DateTimeField(auto_now=True)
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='likes')
    unlike=models.ManyToManyField(User,default=None,blank=True,related_name='unliked')
   


   



class Account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    

    
