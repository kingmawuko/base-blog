from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PostModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    favourites = models.ManyToManyField(User,related_name='favourite',default=None,blank=True)
    
    
    # ratings 
    #image = models.ImageField(upload_to='images', null=True)
  
    def __str__(self):
        return self.title


    @property
    def num_likes(self):
        return self.liked.all.count()
LIKE_CHOICES = (

    ('like', 'like'),
    ('unlike','unlike')
)



class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default="Like" , max_length=10)

    def __str__(self) :
        return str(self.post)






# next time name it as CommentModel
class Comment(models.Model):
    # this represents the post that the comment is for 
    post=models.ForeignKey(PostModel,related_name='comment',on_delete=models.CASCADE,default=True)
    # post_ratings - intiger field max_length = 5 min_length = 1
    # post_rating count 
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # the text they typed 
    comment = models.TextField(null=True)
    date_added=models.DateTimeField(auto_now=True)
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='likes')
    # the comment needs its own likes 


    #like_count =None # this  require an intiger key 
   # comment_count =None 
    
    #reply_comment = None


# the person 
class Account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    # profile picture 
    # username-email

    
