
# this is the feed url 
#IDNETICAL 

from django.urls import *

from .views import *



app_name= 'feed'


urlpatterns = [
    path('',firstpage,name='first'),
    path('first/',firstpage, name='first'),


# this is the detail page of the view that also includes the comment form 
    path('inspect/<int:id>',comment2 , name='inspect'),  # maybe its caling this one instead of 22 

    path('like/<int:id>', like_post ,name='like-post'),
]
 



