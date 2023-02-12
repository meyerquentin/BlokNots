from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, redirect

from . forms import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect('index.html')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login.html')
    form = RegisterForm()
    context = {'form': form}

    return render(request, 'accounts/register.html', context)
