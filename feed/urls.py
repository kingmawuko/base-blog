
# this is the feed url 
#IDNETICAL 

import inspect
from django.urls import *

from .views import *



app_name= 'feed'


urlpatterns = [
   
    


# this is the detail page of the view that also includes the comment form 
    path('inspect/<int:id>',Detail , name='inspect'),  # maybe its caling this one instead of 22 

    path('like/<int:id>', like_post ,name='like-post'),

    # add to favorites function 
    path('fav/<int:id>', add_to_fav ,name='favorite_add'),

    # view the added to favorite 
    path('fav_list/', fav_list ,name='favorite_list'),

    path('',feedpage_view.as_view(),name='first'),

    path('inspect/<int:id>/comment/', Add_comment_class.as_view(),name='add_commento'),


    path('more/',more_view.as_view(),name='more'),
]
 



