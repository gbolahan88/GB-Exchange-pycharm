from django.shortcuts import render

# Home
def home(request):
    return render(request, "home.html", {'navbar': 'home'})

# Blog Page
def blog(request):
    return render(request, "blog.html", {'navbar': 'blog'})

# Rates
def rates(request):
    return render(request, "rates.html", {'navbar': 'rates'})

# Contact Page
def contact(request):
    return render(request, "contact.html", {'navbar': 'contact'})