from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import MyUser

# Create your views here.

class login(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'userAccount/login.html')
	
	def post(self, request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')

def logout(request, *args, **kwargs):
	auth_logout(request)
	return HttpResponseRedirect('/')

class signForm(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'userAccount/sign.html')

	def post(self, request, *args, **kwargs):

		if not request.user.is_authenticated:
			username = request.POST['username']
			nick_name = request.POST['nick_name']
			password = request.POST['password']
			email = request.POST['email']

			try:
				user_model = MyUser.objects.create(username = username, email = email, nick_name=nick_name)
				user_model.set_password(password)
				user_model.save()
				return HttpResponseRedirect('/')

			except:
				return HttpResponse('Username 이나, NickName 이 이미 존재합니다.')
