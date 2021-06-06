from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ReactionButton_home'),
    path('ReactionButton/', views.view_reactionbutton, name='reaction_button'),
    path('PushReaction/', views.push_reaction, name='ReactionButton_push_reaction'),
    path('TestScss/', views.test_scss, name='ReactionButton_test_scss'),
    path('ReactionResult/<int:conf_id>/', views.view_reactionresult, name='ReactionButton_ReactionResult'),
]
