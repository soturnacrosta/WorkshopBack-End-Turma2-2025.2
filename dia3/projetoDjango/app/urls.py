from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    # path('app2/', views.home2, name='app')

]