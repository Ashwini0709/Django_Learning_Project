from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

#These are Class based Views

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class SignUpInterfaceView(CreateView):
    template_name = 'home/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
    


# Create your views here.
"""
These are function based Views

def home(request):
    return render(request, 'home/welcome.html', {'today':datetime.today})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})

"""