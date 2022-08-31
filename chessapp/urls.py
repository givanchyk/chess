from django.urls import path

from . import views

app_name = 'chessapp'
urlpatterns = [
    path('login', views.login_view),
    path('register', views.register),
    path('logout', views.logout_view),
    path('', views.index),
    path('<int:game_id>/', views.game),
]