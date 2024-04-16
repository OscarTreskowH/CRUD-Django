from django.urls import path, include

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('dulces_agregar', views.dulces_agregar, name='dulces_agregar'),
    path('dulces_edit/<str:pkd>', views.dulces_edit, name='dulces_edit'),
    path('dulces_del/<str:pkd>', views.dulces_del, name='dulces_del'),
]