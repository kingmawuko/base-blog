
# this is the feed url 

from django.urls import *

from feed import views as v 


urlpatterns = [
    path('',v.firstpage),
    path('first/',v.firstpage, name='first'),
    path('inspect/<int:id>',v.inspect , name='inspect'),
    path('comment/<int:id>',v.comment , name='comment'),
 


]
