from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from . import views as MyViews

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page="/"), name='logout'),
    path('signup/', MyViews.signup, name='signup'),
    path('auth/', include('social_django.urls', namespace='social')),
]
