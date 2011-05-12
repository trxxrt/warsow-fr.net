from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/users/created/")

    return render_to_response("register.html", {
        'form' : form
    })
