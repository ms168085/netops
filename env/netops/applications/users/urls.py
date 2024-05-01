from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.LoginUser.as_view(), name='user_login'),
    path('logout/', views.LogoutUser.as_view(), name='user_logout'),
]
