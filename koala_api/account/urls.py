from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.user_view, name="users"),
    path('users/create/', views.create_view, name="create"),
    path('auth/', views.login_view, name="login"),
    path('users/profile/', views.profile_view, name="profile"),
]