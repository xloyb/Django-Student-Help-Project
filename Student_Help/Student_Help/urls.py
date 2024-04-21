"""
URL configuration for Student_Help project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
