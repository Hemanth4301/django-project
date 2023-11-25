from django.shortcuts import render

# Create your views here
def home(request):
    return render(request,'home.html')

def products(request):
    return render(request,'products.html')

def service(request):
    return render(request,'service.html')

def  contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')

