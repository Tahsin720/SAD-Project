from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from . models import user, book
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def admin_login(request):
    return render(request, '/admin')