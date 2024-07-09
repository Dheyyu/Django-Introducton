from django.urls import path
from . import views

# Creating our furst url pattern
urlpatterns = [
    path ('', views.post_list, name='post_list'),
#     path ('', views.index, name='index'), # homepage
#     path ('about/', views.about, name='about'), # about page
#     path ('car/', views.car, name='car'), # cars.html page
#     path ('parts/', views.parts, name='parts'), # parts.html page
]
    