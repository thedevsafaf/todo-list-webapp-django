from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from taskmate.context_processors import main_context


def index(request):
    context = {
        "index_text": "Welcome To Taskmate Index Page",
        "title": "Index",
    }
    return render(request, 'web/index.html', context)


def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task has been added successfully"))
        return redirect('todolist_app:todolist')
    else:
        all_tasks = TaskList.objects.all()
        context = {
            "welcome_text": "Welcome To Todo List App",
            "title": "Home",
            "all_tasks": all_tasks,
        }
        return render(request, 'web/todolist.html', context)


def edit_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(TaskList, pk=id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, ("Task has been updated successfully"))
        return redirect('todolist_app:todolist')
    else:
        task_item = get_object_or_404(TaskList, pk=id)
        context = {
            "edit_text": "Update Your Task",
            "title": "Edit Task",
            "task_item": task_item,
        }
        return render(request, 'web/edit.html', context)


def delete_task(request, id):
    task = get_object_or_404(TaskList, pk=id)
    task.delete()
    return redirect('todolist_app:todolist')


def complete_task(request, id):
    task = get_object_or_404(TaskList, pk=id)
    task.done = True
    task.save()
    return redirect('todolist_app:todolist')


def pending_task(request, id):
    task = get_object_or_404(TaskList, pk=id)
    task.done = False
    task.save()
    return redirect('todolist_app:todolist')


def contact(request):
    context = {
        "contact_text": "Welcome To Contact Page",
        "title": "Contact",

    }
    return render(request, 'web/contact.html', context)


def about(request):
    context = {
        "about_text": "Welcome To About Page",
        "title": "About",

    }
    return render(request, 'web/about.html', context)
