from django.shortcuts import render

# Create your views here.
def homeview(request):
    return  render(request,'index.html')


def aboutview(request):
    return render(request,'about.html')

def contactview(request):
    return  render(request,'contact.html')

def kitchenview(request):
    return  render(request,'kitchen.html')

def registerview(request):
    return  render(request,'register.html')

def loginview(request):
    return  render(request,'login.html')





