from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(
                request, "New User added successfully...Login to get Started")
            return redirect('users_app:register')

    else:
        register_form = UserCreationForm()
        context = {
            "register_form": register_form,
        }
        return render(request, 'web/register.html', context)
