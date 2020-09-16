from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from ..models import Movie
import os
import re

# from django.contrib import messages
# messages.add_message(request, messages.INFO, 'Hello world.')

# from ..forms import MovieForm 
  

def index(request):
    if 'user' in request.session:
        movies=Movie.objects.all()
        return render(request,'main.html',{'movies':movies})
    return render(request,'login.html')

def logged_in(request):
    if 'user' in request.session and request.user.is_authenticated:
        movies=Movie.objects.all()
        return redirect('/')
        # return render(request,'main.html',{'movies':movies})
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if not User.objects.filter(username=username).exists():
            return render(request,'login.html',{'error_message':'Please Register First'})
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                request.session['user']=username
                movies=Movie.objects.all()
                return redirect('/')
                # return render(request,'main.html',{'movies':movies})
            else:
                return render(request,'login.html',{'error_message':'Your Account Has Been Suspended'})
        return render(request,'login.html',{'error_message':'Wrong Credentials'})
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        rep_password=request.POST['rep_password']
        e_mail=request.POST['email']
        if User.objects.filter(email=e_mail).exists():
            return render(request,'register.html',{'error_message':'E-mail already registered'})
        elif User.objects.filter(username=username).exists():
            return render(request,'register.html',{'error_message':'Username not available'})
        elif(password!=rep_password):
            return render(request,'register.html',{'error_message':'Passwords Dont match'})
        else:
            user=User(username=username,email=e_mail)
            user.set_password(password)
            user.save()
            user=authenticate(username=username,password=password)
            login(request,user)
            request.session['user']=username
            movies=Movie.objects.all()
            return render(request,'main.html',{'movies':movies})
    return render(request,'register.html')


def log_out(request):
    if 'user' in request.session:
        del request.session['user']
        logout(request)
        return redirect('logged_in')