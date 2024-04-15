from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('home/',login_required(views.home),name='home')
]