from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, Http404
from .forms import UserLoginForm

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')

    user_login_form = UserLoginForm()
    return render(request, 'home/login_page.html', {'login_form': user_login_form})