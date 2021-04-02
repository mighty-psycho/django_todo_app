from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, TodoForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Todo


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back {username.capitalize()}')
            return redirect('todo:todo')

        messages.error(request, 'Invalid username or password')
        return redirect('todo:login')

    return render(request, 'todo/login.html')


def register(request):
    sign_up_form = SignUpForm()
    if request.method == 'POST':
        sign_up_form = SignUpForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Welcome {username.capitalize()}, Your account was successfully crated')
            return redirect('todo:todo')

    return render(request, 'todo/register.html',
                  {'sign_up_form': sign_up_form})


def change_password(request):
    update_pass_form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        update_pass_form = PasswordChangeForm(request.user, request.POST)
        if update_pass_form.is_valid():
            update_pass_form.save()
            messages.info(request, 'Password updated')
            return redirect('todo:login')




    return render(request, 'todo/change_password.html', {'update_pass_form': update_pass_form})


def logout_user(request):
    logout(request)
    messages.info(request, 'You are logged out')
    return redirect('todo:login')


@login_required(login_url='login/')
def todo(request):
    todo_list = Todo.objects.filter(user=request.user)
    todo_form = TodoForm()
    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            new_todo = todo_form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('todo:todo')
    return render(request, 'todo/todo.html',
                  {'todo_list': todo_list,
                   'todo_form': todo_form})


@login_required(login_url='login/')
def delete_todo(request, id):
    if request.method == 'POST':
        todo_id = Todo.objects.get(id=id)
        todo_id.delete()
        return redirect('todo:todo')


@login_required(login_url='login/')
def update_todo(request, id):
    todo_id = Todo.objects.get(id=id)
    if request.method == 'POST':
        new_todo = request.POST['update_todo']
        todo_id.todo = new_todo
        todo_id.save()
        return redirect('todo:todo')
