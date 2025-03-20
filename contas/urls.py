from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register
from .views import profile

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='contas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
