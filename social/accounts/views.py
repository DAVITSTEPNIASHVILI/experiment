from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm, ProfileForm
import random
from django.core.mail import send_mail
from decouple import config
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def profile(req):
    if req.method == 'POST':
        current_user = req.user
        current_user.profile_picture = req.FILES.get('img')
        current_user.save()
    return render(req, 'profile.html')

def user_details(req, id):
    context = {
        'users': User.objects.get(id=id)
    }
    return render(req, 'user_details.html', context)

def register_user(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        verification_code = ''
        alp = 'qwertyuioplkjhgfdsazxcvbnm1234567890'
        for i in range(6):
            verification_code += alp[random.randint(0,len(alp)-1)]

        if form.is_valid():
            req.session['verification_code'] = verification_code
            req.session['user_info'] = form.cleaned_data
            
            send_mail(
                subject='verification code',
                message=f"Your verification code is {verification_code}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data.get('email')]
            )

            return redirect('verification')
        else:
            return render(req, 'register.html', {
                'register_form': form
            })
    context = {
        'register_form': RegisterForm()
    }
    return render(req, 'register.html', context)

def login_user(req):
    if req.method == 'POST':
        # ვიყენებთ Django-ს ჩაშენებულ AuthenticationForm-ს (ან შენს LoginForm-ს), 
        # რომელიც ავტომატურად სწორად ამოწმებს და აჰეშავს პაროლს
        form = LoginForm(req, data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('profile')
        else:
            return render(req, 'login.html', {
                'login_form': form
            })
            
    return render(req, 'login.html', {
        'login_form': LoginForm()
    })

def profile_edit(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        age = req.POST.get('age')
        email = req.POST.get('email')

        current_user = req.user

        current_user.username = username
        current_user.age = age
        current_user.email = email
        current_user.save()
        return redirect('profile')
    context = {
        'profile_form': ProfileForm()
    }
    return render(req, 'profile_edit.html', context)

def verify_user(request):
    verification_code = request.session.get('verification_code')
    user_info = request.session.get('user_info')
    
    if 'user_verification_code' in request.GET:
        if request.GET.get('user_verification_code') == verification_code:
            User.objects.create_user(
                username = user_info.get('username'), 
                email = user_info.get('email'), 
                age = user_info.get('age'), 
                password = user_info.get('password2')
            )
            return redirect('login')
        else:
            return render(request, 'user_verification.html', {
                'error': 'incorrect code'
            })
    return render(request, 'user_verification.html')