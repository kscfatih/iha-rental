from django.shortcuts import render
from django.http import HttpResponse
from .models import Kategori,IHA,KIRALANAN_IHA,User


def dashboard(request):
    if request.user.is_staff:
        user = request.user
        iha = IHA.objects.all().count()
        kiralanan_iha = KIRALANAN_IHA.objects.all().count()
        user_ = User.objects.all().count()
        return render(request,"management/dashboard/index.html",{'user':user,'iha':iha,'kiralanan_iha':kiralanan_iha,'user_':user_})
    else:
        return HttpResponse("Bu sayfayı görüntüleme yetkiniz yok!")
    
