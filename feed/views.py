from django.shortcuts import render,redirect
from . views import *
from . models import * 
from . forms import *
from django.shortcuts import *

# views for feed 



# this needs a dict of all of the posts 
def firstpage(request):
    post=PostModel.objects.all()
    form=CommentForm()
    # if the button is pressed 
  

    context={'post':post,'form':form}
    return render(request,"feed/feed.html",context)




# moght be a different method because the forighn key attaches the comments to a spacific post 
def comments(request,id):
    feed= get_list_or_404(Comment,pk=id) # this should be the comment model 

    context={'feed':feed}
    return render (request,"feed/comments.html",context)