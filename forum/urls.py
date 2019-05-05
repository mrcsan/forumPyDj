from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    path('<int:thread_id>/', views.detail, name='thread'),
    path('login', views.loginView, name='login'),
    path('registration', views.registrationView, name='registration'),
    path('login', views.loginView, name='login'),
    #path('login', auth_views.login, name='login'),
    path('logedin', views.logedinView, name='logedin'),
    path('logout', views.logoutView, name='logout'),
    path('faq', views.faqView, name='faq'),
]
