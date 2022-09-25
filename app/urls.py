

from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('home/', views.home, name='home'),
    path('update/<str:id>/', views.update, name='update'),
    path('read/<str:id>/', views.read, name='read'), #read/1/
    path('delete/<str:id>/', views.delete, name='delete'),

]