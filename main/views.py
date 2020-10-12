from django.shortcuts import render ,redirect , get_object_or_404 , reverse
from django.contrib.auth import logout , login ,authenticate
from django.contrib import messages
from . import forms
from .models import *
from django.http import JsonResponse
import json
from django.core.mail import send_mail


# Create your views here.

def home(request):
    products= Product.objects.filter(remaining__gt = 0)
    
    order , created = Order.objects.get_or_create(customer= request.user.customer , complete=False)

    context = {'products':products,'count':order.totalItems}
    return render(request , 'main/home.html' , context)

def contact(request):
    form = forms.ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'contact from website'
            my_mail = ['mohamad.rafieiyan@yahoo.com']

            message += ' from : ' + email

            send_mail(subject , message , email , my_mail)

            return redirect(reverse('home'))

    context = {'form':form }
    return render(request , 'main/contact.html' , context)


def profile(request):
    order , created = Order.objects.get_or_create(customer= request.user.customer , complete=False)
    context = {'count':order.totalItems}
    return render(request , 'main/profile.html' , context)


def cart(request):

    order , created = Order.objects.get_or_create(customer= request.user.customer , complete=False)
    orderitems = OrderItem.objects.filter(order=order)

    context = {'order':order , 'orderitems':orderitems , 'count':order.totalItems}
    return render(request , 'main/cart.html' , context)

def checkout(request):

    order , created = Order.objects.get_or_create(customer= request.user.customer , complete=False)
    orderitems = OrderItem.objects.filter(order=order)
    
    context = {'count':order.totalItems , 'orderitems':orderitems , 'order':order}
    return render(request , 'main/checkout.html' , context)


def updateCart(request ):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer= request.user.customer
    product = Product.objects.get(id = productId)

    order, created = Order.objects.get_or_create(customer = customer , complete=False)
    orderItem , created = OrderItem.objects.get_or_create(order = order , product=product)
   

    if action == 'add':
        product.remaining -= 1
    else:
        product.remaining += 1

    if not created  and action == 'add':
        orderItem.quantity += 1
        
    elif not created and action == 'remove':
        orderItem.quantity -= 1
        

    product.save()
    orderItem.save()

    if (orderItem.quantity <= 0):
        orderItem.delete()
    
    orderitems = OrderItem.objects.filter(order=order)
    
    return JsonResponse({'TotalCount' : order.totalItems } , safe=False)


# --------------------- registration and login system ------------------------------- 

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password = password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            messages.info(request , "Wrong username or password")
    context = {}
    return render(request , 'main/login.html' , context)


def UserRegisterView(request):

    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save()        
            return redirect(reverse('ProfileRegister' , args=[user.id]))

    context = {'form': form}
    return render(request , 'main/userRegister.html' , context)


def ProfileRegisterView(request , user_pk):

    user = get_object_or_404(User , pk =user_pk)
    form = forms.ProfileForm()

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)    
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = user
            profile.save()
            return redirect('login')
    
    context = {'form' : form}
    return render(request , 'main/profileRegister.html' , context) 

def logoutView(request):
    logout(request)
    return redirect('login')





