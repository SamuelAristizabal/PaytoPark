from django.urls import path
from .views import home_view, register_view, login_view, logout_view

urlpatterns = [
    path("", home_view, name="home"),  # Ruta para la página de inicio
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
