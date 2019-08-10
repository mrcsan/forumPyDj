from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/', views.topicView, name='topic'),
    path('registration', views.registrationView, name='registration'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('faq', views.faqView, name='faq'),
]
