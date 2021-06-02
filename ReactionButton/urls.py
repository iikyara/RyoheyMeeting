from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ReactionButton', views.view_reactionbutton, name='reaction_button'),
    path('PushReaction', views.push_reaction, name='push_reaction'),
    path('TestScss', views.test_scss, name='test_scss'),
]
