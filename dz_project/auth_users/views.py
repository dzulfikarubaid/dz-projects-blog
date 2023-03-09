from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import SignUpForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserProfile(generic.UpdateView):
    form_class = SignUpForm
    template_name = 'profile.html'
    model = User

def GetStarted(request):
    return render(request, 'reg.html')