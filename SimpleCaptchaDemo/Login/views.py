import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from django.contrib import messages 
from django.conf import settings

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        data = request.POST.dict()
        username = data.get('username')
        password = data.get('password')
        recaptcha_response = request.POST.get('g-recaptcha-response')
        print('Username :: '+username)
        print('Password :: '+password)
        if len(username) == 0 or len(password) == 0:
            print('either username or password is empty')
            form = LoginForm()
            messages.error(request, "invalid credentials")
            return render(request, 'index.html',{'form': form})		
		
        if not form.is_valid():
            print('Captcha Failed')
            print('Form Error ',form.errors)
            form = LoginForm()
            messages.error(request, "invalid captcha")
            return render(request, 'index.html',{'form': form})		
			
        return HttpResponse("This is a post request")

    else:
        form = LoginForm()
    return render(request, 'index.html',{'form': form})
