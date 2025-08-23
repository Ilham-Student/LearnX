from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

