
from .forms import RegistrationForm,LoginForm,TaskForm
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # form.clean()
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)    
                return redirect('home')
    else:
         form = LoginForm()

    return render(request,'login.html', {'form': form})
        
def sign_out(request):
    logout(request)
    return redirect('login')
@login_required
def new_task(request):
    if request.method == 'POST':
        forms = TaskForm(request.POST)
        if forms.is_valid():
             
            #  new_task = forms.save(commit=False)
            #  new_task.task =request.user
            task_is = forms.save(commit=False)
            task_is.user = request.user
            task_is.save()
            print('Created')
            return redirect('home')
    else:
        forms = TaskForm()
    return render(request,'add_task.html',{'forms':forms})