from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from .models import Qari
from .forms import UserLoginForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def pricing(request):
    return render(request, 'pricing_info.html')

class QariListView(ListView):
    model = Qari 
    template_name = "qari_list_view.html"

class QariDetailView(DetailView):
    model = Qari 
    template_name = 'qari.html'


