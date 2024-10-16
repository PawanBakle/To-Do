
from .forms import RegistrationForm,LoginForm,TaskForm,EditForm,Completed
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
import pdb; 
from django import template
from django.template.defaulttags import register

register = template.Library()
# Create your views here.
@login_required
def index(request):
    gTask = TaskList.objects.filter(user = request.user)
    # return render(request,'tasks/tasks.html',{'tasks':gTask})
    return render(request,'tasks/index.html',{'tasks':gTask})
   
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # form.clean()
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'tasks/register.html',{'form':form})
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

    return render(request,'tasks/login.html', {'form': form})
        
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
    return render(request,'tasks/add_task.html',{'forms':forms})


def edit_task(request,pk):
    
   
    edit = TaskList.objects.get(id = pk)
   
    if request.method == 'POST':
        edit_form = EditForm(request.POST,instance=edit)

       
        if edit_form.is_valid():
            edit_form.save()
            return redirect('home')
    else:
        edit_form = EditForm(instance=edit)


    return render(request,'tasks/edit_tasks.html',{'post':edit,'etask':edit_form})
@login_required
def all_tasks(request):
    incomplete_tasks = TaskList.objects.filter(is_completed=False)
    completed_tasks = TaskList.objects.filter(is_completed=True)

    # return render(request, 'task_list.html', {
    #     'incomplete_tasks': incomplete_tasks,
    #     'completed_tasks': completed_tasks,
    # })
    gTask = TaskList.objects.filter(user = request.user)
    return render(request,'tasks/tasks.html',{'tasks':gTask,'completed_tasks': completed_tasks})
def is_completed(request,pk):
    task  =get_object_or_404(TaskList, id=pk)
    task.is_completed = True
    task.save()
    return redirect('my_task')
        
        


def post_delete(request,pk):
    post = TaskList.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('my_task')
    context = {
        'post': post
    }
    return render(request, 'tasks/task_delete.html', context)
