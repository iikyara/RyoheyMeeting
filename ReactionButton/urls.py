from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ReactionButton', views.view_reactionbutton, name='reaction_button'),
    path('PushReaction', views.push_reaction, name='push_reaction'),
]