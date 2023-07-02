from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView
from app.models import Product
from app.form import CreateUserForm


# def index(request):
#     return render(request, 'index.html')


class IndexView(ListView):
    template_name = 'index.html'
    model = Product
    queryset = Product.objects.all().order_by('-id')


def about(request):
    return render(request, 'about.html')


# def shop(request):
#     return render(request, 'shop.html')


class ShopView(ListView):
    template_name = 'shop.html'
    model = Product
    queryset = Product.objects.all().order_by('-id')


def contact(request):
    return render(request, 'contact.html')


def testmonial(request):
    return render(request, 'testmonial.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password incorrect')

    context = {}

    return render(request, 'registration/login.html', context)