from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:thread_id>/', views.detail, name='thread'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logedin', views.logedin, name='logedin'),
    path('logout', views.logout, name='logout'),
]
