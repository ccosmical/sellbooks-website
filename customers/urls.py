from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.homepage),
    path('register/', views.register),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]
