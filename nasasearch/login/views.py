from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic


from .forms import LoginForm

class Register(generic.CreateView):
    form_class = UserCreationForm
    model = User
    success_url = reverse_lazy('login:my_login')
    template_name = 'login/register.html'

def my_login(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('login:register'))
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form' : form})

def my_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))