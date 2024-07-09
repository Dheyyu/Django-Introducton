from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def about (request):
    return render(request, 'blog/about.html', {})

def car (request):
    return render(request, 'blog/car.html', {})

def parts(request):
    return render(request, 'blog/parts.html', {})