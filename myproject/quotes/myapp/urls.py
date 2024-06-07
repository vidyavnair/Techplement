from django.urls import path
from.views import home,search,loging,register,logout

urlpatterns = [
    path('',loging,name="loging"),
    path('register/',register,name="register"),
    path('home/',home,name="home"),
    path("search/",search,name="search"),
    path('logout/', logout, name='logout'),
]
