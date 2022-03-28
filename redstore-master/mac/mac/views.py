from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 


def index(request):
     return render(request, 'index.html')

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form =UserCreationForm()


    
  
    return render(request, 'register.html',{'form':form})

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect ('/shop')
        return render(request,'login.html',{'form':form})
    else:
        form = AuthenticationForm()

    return render(request, 'login.html',{'form':form})
