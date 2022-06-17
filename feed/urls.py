
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

    # add to favorites function 
    path('fav/<int:id>', add_to_fav ,name='favorite_add'),

    # view the added to favorite 
    path('fav_list/', fav_list ,name='favorite_list'),

]
 



