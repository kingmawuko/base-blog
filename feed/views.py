from django.shortcuts import *
from django.urls import *
from requests import request # this is for the CBV / the redirect function for ot 
from . views import *
from . models import * 
from . forms import *
from django.shortcuts import *
from django.http import *






 




from django.views.generic import * 
class feedpage_view(View):
            # this is where a button and a form would go    
    def post(self):
        None
        
    def get(self,request):
        post=PostModel.objects.all()
        context={'post':post }
        return render(request,"feed/feed.html",context)


  


    






 #issue: when the submit butttin is pressed is gets saved to the wrong post - this is an id issue 
 # soloution : maybe the action in the form can solve this problem 
 # whats the id in the code doing if its not bringing it to the correct post ? 
 # 
def Detail(request,id): # the issue with the comment has to be here / the issue with the like also roots to here 
    post = get_object_or_404(PostModel, id=id)
    context = {'post':post,}
    return render(request, 'feed/inspect.html', context) 





class Detail_View(DetailView):
    model = PostModel
    template_name = "TEMPLATE_NAME"




def like_post(request,id): 
    user=request.user 
    # this gets skipped with a class based view 
    if request.method =='POST': # if the user presses the like/unlike button      
     # BUG : 
     # Q
     # A
     # this represents the id of the comment that is being liked 
     # the only other place post_id is written is in the inspect .html line 98: in the form the input name is post_id
     # break down the form input 

        post_id =request.POST.get('post_id')  
     

        # BUG: 
        #A
        # post is the varible 
        # postmodel = is the name of the model / why is it postmodel and not the comment 
        # object = is what is used when accesing the functions .get() .all() .filter()
        # get = in here goes the name of the attribute ,  Choices are: comment, description, favourites, id, like, liked, title = 
        # this should be comment / nothing in the post is getting changed only the number of likes in the comment 
        # the single_comment should represent the id of the comment that is beling liked - 
        # its fine in the database but the form is an issue 
        #Q
        # is id supposed to = to a number 
        # what info are we trying to get with the single_comment variable 
                                            
        single_comment = CommentModel.objects.get(post_id = id) # the id of the single comment 
        

       # liked is  the post model 
        if user in single_comment. liked.all():
            single_comment.liked.remove(user)
        else:
            single_comment.liked.add(user)


# BUG : get or create / s
        like,created= Like.objects.get_or_create(user=user,post_id=id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = "Like"
                like.save() # save is not active  
    return redirect('feed:inspect', id=id) # # this is the main differenct - the button is in a inspect instead of the feed - this is not the correct format for bringin in an id
    
# try and make the like comment a cbv

from django.http import *
from django.urls import * # reverse lazy 

def like_post_function(request,id):
    comment=get_object_or_404(CommentModel,id=request.POST.get)
    comment.liked.add(request.user)
    return HttpResponseRedirect(reverse('feed:inspect'))
      

class like_comment_view():
      None 

def rating():
    None




def reply(): # create view 
    None


# bug :
# this is to add an item to the favorites list 
def add_to_fav(request,id): 
    # get this model and if this model does not exist raise the 404 page 
    post=get_object_or_404(PostModel,id=id)

    # if its been added to the favorites do this 
    if post.favourites.exists():

        post.favourites.remove(request.user)

        return render(request,'feed/favorites_list.html') 

        # else do this 
    else:

        post.favourites.add(request.user)

        return render(request,'feed/favorites_list.html')# this should return the user back to where they were before they pressed the add to fav button 
    




def fav_list(request): # this should have an id ? / list view 
   # from the title filter out 
    new = PostModel.title.filter(favourite_list=request.user) # error :'DeferredAttribute' object has no attribute 'filter'
    context={'new':new}
    return render (request,'feed/favorites_list.html',context)









class more_view(ListView):

     def get(self,request):
       
        context={}
        return render(request,"feed/more.html",context)
 





# still the same issue / the problem has to be in the detail view 
class Add_comment_class(CreateView): # this is not where the issue is coming from 
    # this is a form so it has to be a database form type of class 
    model = CommentModel
    fields=['comment']
    success_url: reverse_lazy('first')
   




