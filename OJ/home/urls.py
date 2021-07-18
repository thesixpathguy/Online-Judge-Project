from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path(
        'problem/<int:id>', views.problem, name='problem'),
    path('submitsol/<int:id>', views.submitsol, name='submitsol'),
    path('leaderboard', views.LeaderBoard, name='leaderboard')
]
