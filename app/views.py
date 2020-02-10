from django.shortcuts import render
from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from app.forms import RegisterForm
from restapp.models import DriverUser


def register(request):
    if request.user.is_authenticated:
        return redirect('app:logout')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('userprofile:list')
        else:
            form = RegisterForm()

            args = {'form': form}
            return render(request, 'app/register.html', args)
