import email
from gzip import FNAME
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request, "auth/index.html")
def signup(request):
    
    if request.method == "POST" :
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.phone_no = phoneno
        myuser.save()
        
        messages.success(request,"successfully registered")
        return redirect("/signin")
        
    return render(request, "auth/signup.html")
def signin(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password) 
        if user is not None:
            login(request, user)
            return render(request,"auth/index.html", {'fname': FNAME}) 
        else:
            messages.error(request, "wrong info")
            return redirect('/signup')
    
    
    return render(request, "auth/signin.html")
def signout(request):
   pass