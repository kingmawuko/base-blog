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
   
    # if the button is pressed 
  

    context={'post':post}
    return render(request,"feed/feed.html",context)






# comment and inspect might have to be the same thing 
# this has the original post that the operator created and under here goes the list of comments 
def inspect(request,id): # requires an id - comment b

    
    post= PostModel.objects.get(pk=id)
    comment = Comment.objects.all()
    # comment form to create comment 
    context={'post':post}
    return render(request,'feed/inspect.html',context)




# add comment - login is required to comment  
def comment(request,id): # might need to acess post from the comment model - might need a get_list_404# this also has to have the list of comments 

    # the get object is for getting objects inside of a model 
    post = get_object_or_404(PostModel,id=id) # this has to be the post 


    # if the user pressed the submit button 
    if request.method =='POST':
        # get what they typed in for the comment form 

        # this is used to get the users id - 'user_id' is in the post_detail.html line 65 
        user = User.objects.get(id=request.POST.get('user_id')) 


        # this is the text that the user has typed in the post_detail.html page line 67 
        text = request.POST.get('text')
        # replace author with the creator of the comments account 

        # post is the one that has the related name 
        # text is what the user types in 
        Comment(author=user, post=post, comment=text).save() # this updates the model in the database 
        messages.success(request, "Your comment has been added successfully.")
    else:
        # are these supposed to be different 
        return redirect('inspect.html', id=id)   
    return redirect('inspect.html', id=id) # try without the id 

   


def comment2(request, id):
    # why this and not the other one / why product and not comment - i like id more then slug - what does this thing actually mean 
    selected_product = get_object_or_404(PostModel, id=id)  
    

    review_form = CommentForm()
    if request.method == 'POST': # presses submit 
        review_form = CommentForm(request.POST) 

        # if the form is valid check to see if the user has already  created a comment and print a message 
        if review_form.is_valid(): # if the form is valid 
            # the condition below exists if the form is valid
            if selected_product.productReview.filter(user=request.user).exists(): # if a comment exists 
                messages.info(request, 'You Can Only Review Once...')
            else:
                review_form.save()

                messages.success(request, 'Your Review was Submited successfully')
        
        else: 
            messages.warning(request, 'Failed to submit')


    # get average rating / aggregate ? 
    #avgRate  = Comment.objects.filter(product=selected_product).aggregate(Avg('rate'))

    context = {'selected_product':selected_product, 'review_form':review_form, }
    return render(request, 'feed/inspect.html', context) 











def reply():
    None



