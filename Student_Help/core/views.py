from django.shortcuts import render

def  home(request):
    return render (request, 'home.html')


def  testDashboard(request):
    return render (request, 'dashboard.html')


def  layout(request):
    return render (request, 'layout.html')


def  profile(request):
    return render (request, 'pages/profile.html')

def  register(request):
    return render (request, 'registration/register.html')

def  login(request):
    return render (request, 'registration/login.html')