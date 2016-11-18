from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User

def login_page(request):
	return render(request, "users/login_page.html")

def register(request):
	res = User.objects.register(request.POST)

	if res["added"]:
		request.session["user_id"] = res["new_user"].id
	else:
		for error in res["errors"]:
			messages.error(request, error)

	return redirect("users:login_page")

def login(request):
	user = User.objects.login(request.POST)

	if user:
		request.session["user_id"] = user.id
	else:
		messages.error(request, "E-mail address or password incorrect")

	return redirect("users:login_page")

def logoff(request):
	request.session.clear()
	return redirect("users:login_page")