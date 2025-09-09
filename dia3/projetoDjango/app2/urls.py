from django.urls import path
from . import views

urlpatterns = [
    path('',views.home2, name='home2'),
    path('app/', views.home, name='app')
]