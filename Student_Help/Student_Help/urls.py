from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_view

from core.views import home,Dashboard,layout,profile,register,login

urlpatterns = [
    path('',home), # Default view when accessing root of site
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('dashboard/',Dashboard, name='dashboard'),
    path('t/',layout),
    path('profile/',profile, name='profile'),
    path('register/',register, name='register'),
    #path('login/',login, name='login'),
    path('login/', auth_view.LoginView.as_view(template_name='registration/login.html'), name="login"),
    
]
