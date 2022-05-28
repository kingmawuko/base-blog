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







# this has the original post that the operator created and under here goes the list of comments 
def inspect(request,id): # requires an id - comment b

    
    post= PostModel.objects.get(pk=id)
    comment = Comment.objects.all()
    # comment form to create comment 
    context={'post':post}
    return render(request,'feed/inspect.html',context)




# add comment 
def comment(request,id): # might need to acess post from the comment model - might need a get_list_404
    form=CommentForm() 

    post = get_object_or_404(Comment, pk=id)

    if request.method =='POST':
        form = CommentForm(request.POST) # this might require an id 

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect ('/first/') # this should return to the blog the user just commented on 
    else:
        
        form=CommentForm()
    return render(request, "feed/comments.html", {'form':form})



def reply():
    None



