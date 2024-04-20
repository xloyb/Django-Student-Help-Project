from django.shortcuts import render

def  home(request):
    return render (request, 'home.html')


def  testDashboard(request):
    return render (request, 'dashboard.html')


def  layout(request):
    return render (request, 'layout.html')