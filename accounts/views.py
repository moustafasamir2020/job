from django.shortcuts import render,redirect
from . form import signform
from django.contrib.auth import authenticate ,login
from .models import Profile,city

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form=signform(request.POST)
        if form.is_valid():
            form.save() 
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect ('/accounts/profile')
    else:
        form=signform
    return render (request,'registration/signup.html',{'form':form})


def logout(request):
    
    return render (request,'registration/logged_out.html')


def profile(request):
    pro=Profile.objects.get_or_create(user=request.user)
    
    return render (request,'acc/profile.html',{'p':pro})
