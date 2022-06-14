from django.shortcuts import render,redirect
from . views import *
from . models import * 
from . forms import *
from django.shortcuts import *
from django.views.generic import * 
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Avg
# views for feed 



# this needs a dict of all of the posts 
def firstpage(request):
    post=PostModel.objects.all()
    user=request.user
    context={'post':post ,'user':user}
    return render(request,"feed/feed.html",context)







# comment function
# issue : all comments made link a single post - id issue 
def comment2(request,id):
   

   # the information on the page 
    post = get_object_or_404(PostModel, id=id) 
    form = CommentForm()
    if request.method == 'POST': # presses submit 
        form = CommentForm(request.POST) # form = what the user typed in 
        if form.is_valid(): # if somthing is typed 
                form.save() # save it - save it to the id 
                return redirect ('inspect' ,id=id) # this id method might not work
    context = {'post':post, 'form':form,}
    return render(request, 'feed/inspect.html', context) 





# leave a like 
# the id in the form for like post does not work 
def like_post(request,id): 
    user=request.user
    if request.method =='POST':
        # post will have to be replaced with post model 
        post_id =request.POST.get('post_id')
        post_obj = PostModel.objects.get(id = post_id)
        # if the user has liked the post already
        if user in post_obj . liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like,created= Like.objects.get_or_create(user=user,postmodel_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = "Like"
        like.save()
    return redirect('feed:inspect', id=id) # # this is the main differenct - the button is in a inspect instead of the feed - this is not the correct format for bringin in an id






def rating():
    None




def reply():
    None












