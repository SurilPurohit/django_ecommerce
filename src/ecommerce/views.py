from django.contrib.auth import authenticate,login, get_user_model
from django.http import HttpResponse 
from django.shortcuts import render
from .forms import ContactForm,LoginForm,RegisterForm

def home_page(request):
	context = {
		"title": "Hello World",
		"content": "Welcome to the home page!",
		"premium": "YEAHHHHH"
	}
	# if request.user.is_authenticated():
		# content["premium": "YEAHHHHH"]
	return render(request,"home_page.html",context)

def about_page(request):
	context = {
		"title": "About Page",
		"content": "Welcome to the about page!"
	}
	return render(request,"home_page.html",context)

def contact_page(request):
	contact_form = ContactForm()
	context = {
		"title": "Contact page",
		"content": "Welcome to the contact page!",
		"form": contact_form
	}
	if request.method == "POST":
		print(request.POST.get('fullname'))
		print(request.POST.get('email'))
	return render(request,"contact/views.html",context)

def login_page(request):
	login_form = LoginForm(request.POST or None)
	context = {
		"form": login_form
	}
	# username = form.get("username")
	# password = form.get("password")
	user = authenticate(username='suril', password='suril')
	print(user)
	# print(request.user.is_authenticated())
	if user is not None:
		# print(request.user.is_authenticated())
		login(request,user)
		# return redirect("/login")
	else:
		print("Error")	
	return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
	reg_form = RegisterForm()
	context = {
		"form": reg_form
	}
	if reg_form.is_valid():
		print(reg_form.cleaned_data)
		new_user = User.objects.create_user(username,email,password)
		print(new_user)
	if request.method == "POST":
		print(request.POST.get('username'))
		print(request.POST.get('email'))
		print(request.POST.get('password'))
		print(request.POST.get('password2'))
	return render(request,"auth/login.html",context)

def home_page_old(request):
	return HttpResponse("Hello World!")