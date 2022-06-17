from django.shortcuts import render,redirect
from . views import *
from . models import * 
from . forms import *
from django.shortcuts import *
from django.views.generic import * 

from django.http import HttpResponse, HttpResponseRedirect 



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
def like_post(request,id): # ,post_id,id
    user=request.user
    if request.method =='POST':
        # post will have to be replaced with post model 
        # this comes from the input iname in the inspect page 
        post_id =request.POST.get('post_id')  
        post = PostModel.objects.get(id = post_id) #  
        # if the user has liked the post already
        if user in post . liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)

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


# bug :
# this is to add an item to the favorites list 
def add_to_fav(request,id): 
    post=get_object_or_404(PostModel,id=id)
    # if its been added to the favorites do this 
    if post.favourites.exists():
        post.favourites.remove(request.user)
        return render(request,'feed/favorites_list.html') 
        # else do this 
    else:
        post.favourites.add(request.user)

        return render(request,'feed/favorites_list.html')# this should return the user back to where they were before they pressed the add to fav button 
    




def fav_list(request): # this should have an id ? 
   # from the title filter out 
    new = PostModel.title.filter(favourite_list=request.user) # error :'DeferredAttribute' object has no attribute 'filter'
    context={'new':new}
    return render (request,'feed/favorites_list.html',context)











