
# this is the feed url 

from django.urls import *

from feed import views as v 


urlpatterns = [
    path('',v.firstpage),
    path('first/',v.firstpage, name='first'),
    path('comment/',v.comments , name='comment'), # <int:id>
 


]
