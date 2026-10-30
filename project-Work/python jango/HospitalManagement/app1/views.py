from django.shortcuts import render

def home(request):
    return render(request, 'my.html',{'titles':'Welcome to Hospital Management System'})

def profile(request):
    return render(request, 'profile.html',{'titles':'Welcome to Hospital Management System'})
def expressions(request):
    return render(request,'output.html')