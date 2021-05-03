from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import CreateUserForm

from .decorators import unauthenticated_user, allowed_users, admin_only



@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('creator_profile')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'creator/signin.html', context)

def logoutUser(request):
	logout(request)
	return redirect('signin')


@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			#Added username after video because of error returning customer name if not added
			Customer.objects.create(
				user=user,
				name=user.username,
				)

			messages.success(request, 'Account was created for ' + username)

			return redirect('signin')
		

	context = {'form':form}
	return render(request, 'creator/signup.html', context)

@login_required(login_url="/creator/signin")
def creatorprofile(request):
    thank = False
    if request.method=="POST":
        first = request.POST['first']
        last = request.POST['last']
        phone = request.POST['phone']
        email = request.POST['email']
        youtube = request.POST['youtube']
        instagram = request.POST['instagram']
        facebook = request.POST['facebook']
        snapchat = request.POST['snapchat']
        cat1 = request.POST['cat1']
        cat2 = request.POST['cat2']
        cat3 = request.POST['cat3']
        cat4 = request.POST['cat4']
        profile = Creator(first=first, last=last,phone=phone,email=email, 
        youtube=youtube,instagram=instagram,facebook=facebook,snapchat=snapchat,
        cat1=cat1,cat2=cat2,cat3=cat3,cat4=cat4)
        profile.save()
        
        thank = True
    return render(request, 'creator/creator_profile.html', {'thank': thank})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	

	context = {'customer':customer}
	return render(request, 'creator/creator_profile.html',context)