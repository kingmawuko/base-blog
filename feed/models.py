from django.db import models

# Create your models here.


class PostModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    # ratings 
    #image = models.ImageField(upload_to='images', null=True)
  
    

    def __str__(self):
        return self.title


# should be able to edit/delete post 
class Comment(models.Model):
    person=None
    comment = models.CharField(max_length=50)
    date_added=None
    like =None
    dislike =None
    reply_comment = None


# the person 
class Account(models.Model):
    None
    # username-email

    
