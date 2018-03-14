from django.shortcuts import render

def index(request):
    render(request, 'frontend/index.html')
