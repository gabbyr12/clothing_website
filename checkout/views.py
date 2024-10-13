from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def fly(request):
    return render(request, 'fly.html')
