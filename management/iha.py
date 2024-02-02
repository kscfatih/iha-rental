from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IHASerializer ,KategoriSerializer,KIRALANAN_IHASerializer,UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import JsonResponse , HttpResponse , HttpResponseRedirect
from .models import IHA , Kategori , KIRALANAN_IHA
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required(login_url='/panel/login')
def create(request):
    if request.user.is_staff:
        kategoriler = Kategori.objects.all()
        if request.method == 'POST':
            marka = request.POST.get('marka')
            model = request.POST.get('model')
            agirlik = request.POST.get('agirlik')
            kategori = request.POST.get('kategori')
            ucus_suresi = request.POST.get('ucus_suresi')
            menzil = request.POST.get('menzil')
            navigasyon = request.POST.get('navigasyon')=='true'
            yuk_kapasitesi = request.POST.get('yuk_kapasitesi')
            oto_pilot = request.POST.get('oto_pilot') =='true'
            maksimum_hiz = request.POST.get('max_hiz')
            resim = request.FILES.get('resim') 
            status = request.POST.get('status')
            kategori_selected = Kategori.objects.get(id = kategori )
            yeni_iha = IHA(
                marka=marka,
                model=model,
                agirlik=agirlik,
                navigasyon =navigasyon,
                kategori=kategori_selected,
                ucus_suresi=ucus_suresi,
                menzil=menzil,
                yuk_kapasitesi=yuk_kapasitesi,
                oto_pilot=oto_pilot,
                maksimum_hiz=maksimum_hiz,
                resim=resim,
                status=status
            )

            yeni_iha.save()

            messages.success(request, 'İHA başarıyla eklendi.')
            return redirect('management:list-iha')  
        else:
            return render(request, "management/IHA/create.html" , {"kategori" : kategoriler})
        
    else:
        return HttpResponse("Bu sayfayı görüntüleme yetkiniz yok!")
    




@login_required(login_url='/panel/login')
def iha_duzenle(request , id):
    iha = IHA.objects.get(id = id)
    kategoriler = Kategori.objects.all()
    if request.method =="POST":
        marka = request.POST.get('marka')
        model = request.POST.get('model')
        agirlik = request.POST.get('agirlik')
        kategori = request.POST.get('kategori')
        ucus_suresi = request.POST.get('ucus_suresi')
        menzil = request.POST.get('menzil')
        navigasyon = request.POST.get('navigasyon')
        yuk_kapasitesi = request.POST.get('yuk_kapasitesi')
        oto_pilot = request.POST.get('oto_pilot') 
        maksimum_hiz = request.POST.get('max_hiz')
        if 'resim' in request.FILES:
            resim = request.FILES['resim']
            iha.resim = resim
        status = request.POST.get('status')
        kategori_selected = Kategori.objects.get(id = kategori )

        iha.marka = marka
        iha.model = model
        iha.agirlik = agirlik
        iha.ucus_suresi = ucus_suresi
        iha.menzil = menzil
        iha.kategori = kategori_selected
        iha.yuk_kapasitesi = yuk_kapasitesi
        iha.navigasyon = navigasyon
        iha.oto_pilot = oto_pilot
        iha.maksimum_hiz = maksimum_hiz
        iha.status = status
        iha.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return render(request , "management/IHA/create.html" , {"iha" : iha , "kategori" : kategoriler})

@login_required(login_url='/panel/login')
def list(request):

    kategoriler = Kategori.objects.all()

    return render(request,"management/IHA/list.html",{'kategoriler':kategoriler})

@login_required(login_url='/panel/login')
def edit_category(request,id):
    if request.method == "POST":
       isim = request.POST.get('isim')
       tanim = request.POST.get('tanim')
       kategori = Kategori.objects.get(id = id )
       kategori.isim = isim
       kategori.tanim = tanim
       kategori.save()
       messages.success(request, 'Kategori başarıyla güncellendi.')
       return redirect('management:category-list')
    kategori = Kategori.objects.get(id = id )
    return render(request, "management/category/edit.html",{'kategori':kategori})


@login_required(login_url='/panel/login')
def create_category(request):
    if request.method == "POST":
        isim = request.POST.get('isim')
        tanim = request.POST.get('tanim')
        task = Kategori(isim = isim , tanim=tanim)
        task.save()
        messages.success(request, 'Kategori başarıyla eklendi.')
        return redirect('management:category-list')
    return render(request, "management/category/create.html")


@login_required(login_url='/panel/login')
def kategori_list_view(request):
    return render(request,"management/category/list.html")


@login_required(login_url='/panel/login')
def kategori_sil(request,id):
    Kategori1 = Kategori.objects.get(id = id )
    Kategori1.delete()
    return redirect('management:category-list')

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6  
    page_size_query_param = 'page_size'
    max_page_size = 100
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_items': self.page.paginator.count,  
            'total_pages': self.page.paginator.num_pages,  
            'current_page': self.page.number, 
            'results': data
        })
    

@api_view(['GET'])
def kategori_list(request):
    search_query = request.GET.get('search', '')
    kategori_obj = Kategori.objects.all().order_by('-id')
    if search_query:
        kategori_obj = kategori_obj.filter(
            Q(isim__icontains=search_query) |
            Q(tanim=search_query)
        )
    
    
    paginator = StandardResultsSetPagination()
    result_page = paginator.paginate_queryset(kategori_obj, request)
    serializer = KategoriSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@login_required(login_url='/panel/login')
def kiralanan_list(request):
    kategoriler = Kategori.objects.all()
    return render(request,"management/IHA/hire/list.html",{'kategoriler':kategoriler})

@login_required(login_url='/panel/login')
def user_list_(request):
    return render(request,"management/IHA/user.html")

@login_required(login_url='/panel/login')
def user_sil(request,id):
    user = User.objects.get(id = id )
    user.delete()
    messages.success(request,'Kullanıcı başarı ile silindi')
    return redirect("management:user-list")

@api_view(['GET'])
def user_list(request):
    search_query = request.GET.get('search', '')
    users = User.objects.all()
    if search_query:
        users = users.filter(
            Q(first_name__icontains=search_query) | 
            Q(last_name__icontains=search_query) |
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    paginator = StandardResultsSetPagination()
    result_page = paginator.paginate_queryset(users, request)
    serializer = UserSerializer(result_page, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def kiralanan_iha_list(request):
    user = request.user
    search_query = request.GET.get('search', '')
    kiralanan_objects = KIRALANAN_IHA.objects.filter(user=user).order_by('-id')
    if request.user.is_staff:
        kiralanan_objects = KIRALANAN_IHA.objects.all().order_by('-id')
    menzil_filter = request.GET.get('menzil', '')
    yuk_kapasitesi_filter = request.GET.get('yuk_kapasitesi', '')
    kategori_filter = request.GET.get('kategori', '')
    status_filter = request.GET.get('status', '')

    if status_filter:
        kiralanan_objects = kiralanan_objects.filter(status=status_filter)

    if menzil_filter:  
        min_menzil, max_menzil = map(int, menzil_filter.split('-'))
        kiralanan_objects = kiralanan_objects.filter(iha__menzil__gte=min_menzil, iha__menzil__lte=max_menzil)

    if yuk_kapasitesi_filter:
        min_yuk, max_yuk = map(int, yuk_kapasitesi_filter.split('-'))
        kiralanan_objects = kiralanan_objects.filter(iha__yuk_kapasitesi__gte=min_yuk, iha__yuk_kapasitesi__lte=max_yuk)
        
    if kategori_filter:
       kiralanan_objects = kiralanan_objects.filter(iha__kategori__id=kategori_filter)
    

    if search_query:
        kiralanan_objects = kiralanan_objects.filter(
            Q(iha__marka__icontains=search_query) | 
            Q(iha__model__icontains=search_query) |
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query)
        )

    paginator = StandardResultsSetPagination()
    result_page = paginator.paginate_queryset(kiralanan_objects, request)
    serializer = KIRALANAN_IHASerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def iha_list(request):
    search_query = request.GET.get('search', '')
    menzil_filter = request.GET.get('menzil', '')
    yuk_kapasitesi_filter = request.GET.get('yuk_kapasitesi', '')
    kategori_filter = request.GET.get('kategori', '')
    iha_objects = IHA.objects.all().order_by('-id')

    if search_query:
        iha_objects = iha_objects.filter(
            Q(marka__icontains=search_query) |
            Q(model__icontains=search_query)
        )

    if menzil_filter:  
        min_menzil, max_menzil = map(int, menzil_filter.split('-'))
        iha_objects = iha_objects.filter(menzil__gte=min_menzil, menzil__lte=max_menzil)

    if yuk_kapasitesi_filter:
        min_yuk, max_yuk = map(int, yuk_kapasitesi_filter.split('-'))
        iha_objects = iha_objects.filter(yuk_kapasitesi__gte=min_yuk, yuk_kapasitesi__lte=max_yuk)
        
    if kategori_filter:
       iha_objects = iha_objects.filter(kategori__id=kategori_filter)

    paginator = StandardResultsSetPagination()
    result_page = paginator.paginate_queryset(iha_objects, request)
    serializer = IHASerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)



@login_required(login_url='/panel/login')
def iha_sil(request, id):
    iha = IHA.objects.get(id = id )
    iha.delete()
    messages.success(request, "Başarılı!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



@login_required(login_url='/panel/login')
def iha_kiralama(request):
    if request.method == "POST":
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        iha_id = request.POST.get('iha_id')
        iha = IHA.objects.get(id = iha_id)
        user = request.user
        existing_request = KIRALANAN_IHA.objects.filter(user=user, iha_id=iha_id).exists()
        if existing_request:
            messages.error(request, "Zaten bu İHA için talep oluşturdunuz!")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        task = KIRALANAN_IHA(iha=iha , user = user , baslangic_tarihi = start_date , bitis_tarihi = end_date , status = "PENDING")
        task.save()
        messages.success(request, "Başarılı!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    



@login_required(login_url='/panel/login')
def kiralanan_iha_sil(request , id):
    kiralanan_iha = KIRALANAN_IHA.objects.get(id = id)
    kiralanan_iha.delete()
    messages.success(request, "Başarılı!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




@login_required(login_url='/panel/login')
def kiralanan_iha_onay(request , id):
    kiralanan_iha = KIRALANAN_IHA.objects.get(id = id)
    kiralanan_iha.status = "ACTIVE"
    kiralanan_iha.save()
    messages.success(request, "Başarılı!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
