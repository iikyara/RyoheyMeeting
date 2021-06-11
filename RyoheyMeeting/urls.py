"""RyoheyMeeting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    # home
    path('', include('home.urls')),

    # deal to projects
    path('ReactionButton/', include('ReactionButton.urls')),
    path('ReactionSocket/', include('ReactionSocket.urls')),

    # for admin
    path('admin/', admin.site.urls),

    # for login
    #path('registration/login/', views.LoginView.as_view(), name='login'),
    #path('registration/logout/', views.LogoutView.as_view(next_page="/"), name='logout'),
    #path('signup/', include('accounts.urls'), name='signup'),
    #path('auth/', include('social_django.urls', namespace='social')),
    path('registration/', include('accounts.urls')),
]
