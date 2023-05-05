from django.urls import path
from videoapp import views

urlpatterns = [
    path("", views.index, name='index'),
]
