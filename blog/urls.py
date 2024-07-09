from django.urls import path
from . import views

# Creating our furst url pattern
urlpatterns = [
    path ('', views.index, name='index'),
]