from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home',views.home, name='home'),
    path('add_video',views.add_video,name='add_video'),
    path('login/',views.login_view,name='login'),
    path('registration/',views.registration,name='registration'),
    path('logout/',views.Logout,name='logout'),

]
