from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.


# def register_view(request):
#     return render(request, 'accounts/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, "You have successfully logged in. Welcome")
            return HttpResponseRedirect(reverse('home_view'))

    return HttpResponseRedirect(reverse('home_view'))


def logout_view(request):

    logout(request)
    messages.success(
        request, 'You have successfully logged out. You can login or roam around elsewhere!')
    return HttpResponseRedirect(reverse('home_view'))
