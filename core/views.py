from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def article(request):
    return render(request, 'article-details.html')

def privacy(request):
    return render(request, 'privacy-policy.html')

def terms(request):
    return render(request, 'terms-conditions.html')

def login(request):
    return render(request, 'log-in.html')

def signup(request):
    return render(request, 'sign-up.html')