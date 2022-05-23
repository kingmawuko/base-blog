from django.shortcuts import render,redirect
from . views import *
from . models import * 
from . forms import *
from django.shortcuts import *

# views for feed 



# this needs a dict of all of the posts 
def firstpage(request):
    post=PostModel.objects.all()
   
    # if the button is pressed 
  

    context={'post':post}
    return render(request,"feed/feed.html",context)




# this button is in the inspect page and it is a form / 
def comments(request):
    feed= get_list_or_404(Comment) # this should be the comment form - filling out the comment section 

    context={'feed':feed}
    return render (request,"feed/comments.html",context)



# this has the original post that the operator created and under here goes the list of comments 
def inspect(request,id): # requires an id - comment b
    
    post=get_list_or_404(PostModel,pk=id)
    comment = Comment.objects.all()
    # comment form to create comment 
    context={'post':post}
    return render(request,'feed/inspect.html',context)