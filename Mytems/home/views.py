from django.shortcuts import render


def index(request):
    return render(request, 'category.html', {})


def error(request):
    return render(request, '404.html', {})


def detail(request):
    return render(request, 'detail.html', {})


def faq(request):
    return render(request, 'faq.html', {})


def sign_in(request):
    return render(request, 'sign-in.html', {})


def add_book(request):
    return render(request, 'add_book.html', {})


def add_clothes(request):
    return render(request, 'add_clothes.html', {})


def add_medicine(request):
    return render(request, 'add_medicine.html', {})


def add_tech(request):
    return render(request, 'add_tech.html', {})
