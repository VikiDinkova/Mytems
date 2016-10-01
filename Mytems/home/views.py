from django.contrib.auth import login as login_user, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Drug, Clothes, TechAccessory, Book


def index(request):
    drugs_all = Drug.objects.all()
    clothes_all = Clothes.objects.all()
    tech_accessories_all = TechAccessory.objects.all()
    books_all = Book.objects.all()
    context = {
        'drugs': drugs_all,
        'clothes': clothes_all,
        'tech_accessories': tech_accessories_all,
        'books': books_all
    }
    return render(request, 'category.html', context)


def error(request):
    return render(request, '404.html', {})


def sign_in(request):
    data = {
        'error': None,
    }
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            if user is None:
                raise User.DoesNotExist
            if user.is_active:
                login_user(request, user)
                return redirect('borrowers:home')
            else:
                data['error'] = 'user_inactive'
        except User.DoesNotExist:
            data['error'] = 'user_does_not_exist'
    return render(request, 'sign-in.html', {})


def add_book(request):
    return render(request, 'add_book.html', {})


def add_clothes(request):
    return render(request, 'add_clothes.html', {})


def add_medicine(request):
    return render(request, 'add_medicine.html', {})


def add_tech(request):
    return render(request, 'add_tech.html', {})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
            )
            user.set_password(request.POST['password'])
            user.save()
    return redirect('home:index')


def logout_user(request):
    logout(request)
    return redirect('home:index')


def drugs(request):
    all_drugs = Drug.objects.all()
    context = {
        'drugs': all_drugs
    }
    return render(request, 'drugs.html', context)


def clothes(request):
    all_clothes = Clothes.objects.all()
    context = {
        'clothes': all_clothes
    }
    return render(request, 'clothes.html', context)


def techaccessoaries(request):
    all_tech = TechAccessory.objects.all()
    context = {
        'tech': all_tech
    }
    return render(request, 'tech.html', context)
