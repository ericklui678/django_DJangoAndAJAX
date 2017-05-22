from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'djangoAJAX_app/index.html')
def message(request):
    return HttpResponse('Hello from the server!')
