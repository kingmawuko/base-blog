from django.shortcuts import render,redirect
from . views import *
from . models import * 
from . forms import *

# Create your views here.



# this needs a dict of all of the posts 
def firstpage(request):

    post=PostModel.objects.all()
    context={'post':post}

    return render(request,"feed/feed.html",context)