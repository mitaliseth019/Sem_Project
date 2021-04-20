from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Contact
from math import ceil
import json
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth
from django.contrib.auth import login
# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'

def index(request):
    
    return render(request, 'home/index.html')
def about(request):
    
    return render(request, 'home/about.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
       
        if username and password:

            #user  = auth.authenticate(username = username, password= password)
            if User.objects.filter(username = username).exists():
                user = auth.authenticate(username = username, password = password )
            else:
                user = User.objects.get(email = username)
                user = auth.authenticate(username = user.username, password = password )
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "username or password is Incorrect")

        else:
            messages.error(request, "Fill out all feilds")
    
    return render(request, 'home/signin.html')
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username Taken")
            return render(request,'home/signup.html', {})
        elif User.objects.filter(email=email).exists():
            return render(request,'home/signup.html', {})
        else:
            user = User.objects.create_user(first_name = first_name, username = username, email = email, password = password)
            user.save()
            return redirect('signin')
    else:
        return render(request, 'home/signup.html')

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
        thank = True
    return render(request, 'home/contact.html', {'thank': thank})


# Create your views here.
