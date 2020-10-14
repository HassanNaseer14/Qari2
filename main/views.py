from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from .models import Qari
from .forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, 'home.html')


def pricing(request):
    return render(request, 'pricing_info.html')


class QariListView(ListView, LoginRequiredMixin):
    login_url = '/login/'
    
    model = Qari
    template_name = "qari_list_view.html"


class QariDetailView(DetailView, LoginRequiredMixin):
    model = Qari
    template_name = 'qari.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
