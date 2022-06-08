
# this is the feed url 
#IDNETICAL 

from django.urls import *

from .views import *


urlpatterns = [
    path('',firstpage,name='first'),
    path('first/',firstpage, name='first'),


# this is the detail page of the view that also includes the comment form 
    path('inspect/<int:id>',comment2 , name='inspect'),  # maybe its caling this one instead of 22 


# the error cpde redirects pack to this page / maybe i need an app name 
# error code : Reverse for 'commento' with arguments '('',)' not found. 1 pattern(s) tried: ['inspect/(?P<id>[0-9]+)/comment/\\Z']
    
 


]
