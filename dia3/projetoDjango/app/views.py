from django.shortcuts import render

# Create your views here.
# def home(request):
#    return render(request, "home.html")

# from django.http import HttpResponse

def home(request):
    return render(request, 'app/home.html')