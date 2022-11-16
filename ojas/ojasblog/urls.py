from django.urls import path 

from . import views 

urlpatterns = [
    path('singup',views.signing,name="signpage"),
    path('login',views.loging,name="logpage"),
    path('home',views.home,name="homepage"),
    path('about',views.about,name="aboutpage"),
    path('contact',views.contating,name="contactpage"),
    path('showdashbord',views.showdashbord,name="dashbordpage"),
    path('logout',views.lout,name="logoutpage"),
    path('blog',views.detialsform,name="blogpage"),
    path('<int:id>',views.updatedata,name="updateing"),
    path('delete/<int:id>',views.deletedata,name="deleting"),
    path('p',views.add_blog)
]
