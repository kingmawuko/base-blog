

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.forms import RegisterForm







def Login(request):
    # if the user presses submit 
    if request.method == 'POST': # post means your sending data back
        # label what they have imputted for the fields 
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # if the username inputted is not in the databasw 
            user = User.objects.get(username=username) 
        except:
            # print this 
            messages.error(request, 'User does not exist') # print this 

        user = authenticate(request, username=username, password=password)

        # if the user exists 
        if user is not None:
            login(request, user)
            return redirect('/first/') # feed is in ... 
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request,'users/login.html')
   
def Logout(request):
    logout(request)
    return redirect('/login/') 

def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        # return redirect ('\ \')
        # or return a message that theyre account has been created 
    else:
        form=RegisterForm()
    return render(response,'users/register.html',{'form':form})