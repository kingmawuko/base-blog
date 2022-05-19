# urls for accounts 

# / login/register/reset pw / settings 



from django.urls import path
from . import views




urlpatterns = [
    # this is the first page 



    path("",views.Login,name="login"),
    path("login/",views.Login,name="login"),
    path("logout/",views.Logout,name="logout"),
    path("register/",views.register,name="register"),


    


   # path("feed/",views.Main_feed,name="feed"),





# when the user is logged in take em to this page 
 
]