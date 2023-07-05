from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import AppDetails
from .decorators import login_required
# Create your views here.

@login_required
def Home(request):
    All_apps = AppDetails.objects.all()
    return render(request, 'home.html', {'app_details': All_apps, 'user': request.user,})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user,})

@login_required
def submit_img(request,App_id):
    All_apps = AppDetails.objects.filter(id=App_id)
    return render(request, 'submit_img.html', {'app_details': All_apps, 'user': request.user, })

@login_required
def task(request):
    All_apps = AppDetails.objects.all()
    return render(request, 'task.html', {'app_details': All_apps, 'user': request.user,})

@login_required
def points(request):
    All_apps = AppDetails.objects.all()
    return render(request, 'points.html', {'app_details': All_apps, 'user': request.user,})

@login_required
def Add_App(request):
    if request.method == 'POST':
        AppIcon = request.FILES.get('AppIcon')
        AppName = request.POST.get('AppName')
        AppLink = request.POST.get('AppLink')
        AppCategory = request.POST.get('AppCategory')
        AppSubCategory = request.POST.get('AppSubCategory')
        points = request.POST.get('points')

        if AppDetails.objects.filter(AppName=AppName).exists():
            messages.error(request, 'Invalid App Already Exist')
            return render(request, 'Add_App.html')
        else:
            Appdetails = AppDetails(AppIcon=AppIcon, AppName=AppName, AppLink=AppLink, AppCategory=AppCategory, AppSubCategory=AppSubCategory, points=points)
            Appdetails.save()
            messages.success(request, 'Form submitted successfully!')
            return render(request, 'Add_App.html')
    else:
        return render(request, 'Add_App.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('Home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')

def register (request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('login')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                user.save()
                messages.info(request, 'registration successful')
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
"""
AppIcon
AppName
AppLink
AppCategory
AppSubCategory
points
"""