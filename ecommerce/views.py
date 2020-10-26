from django.shortcuts import render, redirect 
from django.http import HttpResponse

from .models import *
from .form import *


def home(request):
        products = Product.objects.all()
        users = User.objects.all()
        products_bought = Product_bought.objects.all()
        context = {'products':products, 'users':users, 'product_bought':products_bought}
        return render(request, 'ecommerce/dashboard.html', context)

def products(request, pk_test):
        products = Product.objects.all()
        product = Product.objects.get(id=pk_test)

        orders = Product_bought.objects.get(product_id=pk_test)

        context = {'products':products,'product_search':product, 'orders':orders}
        return render(request, 'ecommerce/products.html', context)

def users(request, pk_test):
        users = User.objects.all()
        user = User.objects.get(id=pk_test)

        orders = Product_bought.objects.get(user_id=pk_test)

        context = {'user':user, 'orders':orders}
        return render(request, 'accounts/customer.html',context)

def orders(request, pk_test1, pk_test2):
        orders = Product_bought.objects.all()
        order = Product_bought.objects.get(user_id=pk_test1, product_id=pk_test2)

        context = {'order_search':order, 'orders':orders}
        return render(request, 'ecommerce/orders.html', context)

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'ecommerce/order_form.html', context)

def updateOrder(request, pk):

	order = Product_bought.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'ecommerce/order_form.html', context)

def deleteOrder(request, pk):
	order = Product_bought.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'ecommerce/delete_order.html', context)

def createUser(request):
	form = UserForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'ecommerce/order_form.html', context)

def updateUser(request, pk):

	user = User.objects.get(id=pk)
	form = UserForm(instance=user)

	if request.method == 'POST':
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'ecommerce/order_form.html', context)

def deleteUser(request, pk):
	user = User.objects.get(id=pk)
	if request.method == "POST":
		user.delete()
		return redirect('/')

	context = {'item':user}
	return render(request, 'ecommerce/delete_user.html', context)

def createProduct(request):
	form = ProductForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'ecommerce/order_form.html', context)

def updateProduct(request, pk):

	product = Product.objects.get(id=pk)
	form = ProductForm(instance=product)

	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'ecommerce/order_form.html', context)

def deleteProduct(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == "POST":
		product.delete()
		return redirect('/')

	context = {'item':product}
	return render(request, 'ecommerce/delete_product.html', context)
