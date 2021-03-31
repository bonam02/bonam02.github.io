from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Product

user = ''
flag = True
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		print("form ::: ",form.is_valid())
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("polls/login.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render(request=request, template_name="polls/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		print("coming or nor",User.objects.all())
		form = AuthenticationForm(request, data=request.POST)
		username = request.POST['username']
		password = request.POST['password']
		global user
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("success.html",user=user)
		else:
			return redirect("failure.html")

	form = AuthenticationForm()
	return render(request=request, template_name="polls/login.html", context={"login_form":form})


def getData():
	p = Product(product='Apple', user_name='bonam',p_id = 1,product_price=2000)
	p.save()
	p = Product(product='Samsung', user_name='bonam1', p_id=1, product_price=3000)
	p.save()
	p = Product(product='Sony', user_name='bonam', p_id=2, product_price=2400)
	p.save()
	p = Product(product='RealMe', user_name='bonam1', p_id=2, product_price=2500)
	p.save()
	return Product.objects.all()

def success(request):
	global flag
	if flag:	# As time being stopping data base logic using global flag
		data = getData();
		flag = False
	get_user_data = Product.objects.all()
	list_data = []
	for product in get_user_data:
		dict_map = {}
		if str(product.user_name).strip() == str(user).strip():
			dict_map["p_id"] = product.p_id
			dict_map["user_name"] = product.user_name
			dict_map["product"] = product.product
			dict_map["product_price"] = product.product_price
			list_data.append(dict_map)
	return render(request, 'polls/success.html',{"list_data":list_data})

def failure(request):
	return render(request, 'polls/failure.html')