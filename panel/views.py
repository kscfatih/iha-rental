from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password

@login_required(login_url='/panel/login')
def dashboard(request):
    return render(request,"panel/IHA/hire.html" , {"user" : request.user})

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        paramatere = User.objects.get(email=email)
        username = paramatere.username
        usercontrol = authenticate(request, username=username, password=password)
        if usercontrol is not None:
            login(request, usercontrol)
            if request.user.is_staff:
                return redirect('management:dashboard')
            else:
                return redirect('panel:dashboard')

        else:
            messages.error(request, "Giriş yapılırken bir hata oluştu. Lütfen tekrar deneyiniz...")
            return redirect('panel:login')
        
    elif request.user.is_authenticated:
            return redirect('panel:dashboard')    
    else:
        return render(request,"panel/login/login.html")

def register_user(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = firstname.lower() + lastname.lower() + str(random.randint(1000, 9999))
        email = request.POST.get("email")
        pw1 = request.POST.get("pw1")
        pw2 = request.POST.get("pw2")
        if User.objects.filter(email=email).exists():
           messages.error(request, "Bu email daha önce kullanılmış.")
           return redirect('panel:register')
        if pw1 == pw2:
            user_kayit = User.objects.create_user(username=username, is_active=True, email=email, password=pw1, first_name=firstname, last_name=lastname)
            user_kayit.save()
            return redirect('panel:dashboard' )
        else:
            messages.error(request, "Şifreler eşleşmiyor!")
            return redirect('panel:register' )
    else:
        return render(request,"panel/login/register.html")
    
def logout_user(request):
    logout(request)
    return redirect('panel:login')

@login_required(login_url='/panel/login')
def account(request):
    id=request.user.id
    User = get_user_model()
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        firstname = request.POST.get("first_name")
        lastname = request.POST.get("last_name")
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    return render(request,"panel/login/account.html" , {"user" : user})

def password_change(request):
    user_id=request.user.id
    user = get_user_model().objects.get(id=user_id)
    if request.method == 'POST':
        current = request.POST.get('current')
        pw1 = request.POST.get('pw1')
        pw2 = request.POST.get('pw2')
        if pw1 == pw2 and check_password(current, user.password):
            user.set_password(pw1)
            user.save()
            return redirect('panel:logout')
        else:
            pass
    return render(request, "panel/login/repassword.html")


def home(request):
    return render(request,"panel/home.html")
