from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def pricing(request):
    return render(request, 'pricing_info.html')