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
