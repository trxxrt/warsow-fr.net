from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def home(requets):
    return render_to_response("home.html")

