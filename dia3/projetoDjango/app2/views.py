from django.shortcuts import render

# Create your views here.
def home2(request):
    return render(request, 'home2.html')

def home(request):
    return render(request, 'home.html')