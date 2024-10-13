from django.contrib import admin
from django.urls import path
from .views import home, about, ai, register, user_login, user_logout,forminfo,user_details,update_user_details

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home1"),
    path("home/about-us", about, name="about"),
    path("home/ai", ai, name="ai"),
    path("home/register", register, name="register"),
    path("home/login", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path('user-details/', user_details, name='user_details'),
    path('update-details/', update_user_details, name='update_user_details'),
    # path("detail/", detail, name="detail"),  # Changed to require user details
    path("form/", forminfo, name="forminfo"),
]
