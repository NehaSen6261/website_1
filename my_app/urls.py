from django.urls import path
from my_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('home', views.home, name="home"),
    path('login', views.login, name="login")
]