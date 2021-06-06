from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('conferencelist/', views.conferencelist, name='conferencelist'),
    path('conferenceinfo/<int:conf_id>/', views.conferenceinfo, name='conferenceinfo'),
    path('usersetting/', views.usersetting, name='usersetting'),

    #for entry
    path('entry/<int:conf_id>/', views.entry, name='entry'),
    path('getispresenter/<int:conf_id>/', views.getIsPresenter, name='getispresenter'),
    path('setpresenter/<int:conf_id>/<int:is_participate>/', views.setPresenter, name='setpresenter'),
]
