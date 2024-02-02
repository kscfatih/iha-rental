from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirect_to_dashboard(request):
    return redirect('panel:home')

urlpatterns = [
    path('', redirect_to_dashboard, name='home'),
    path('admin/', admin.site.urls),
    path('panel/',include('panel.urls')),
    path('management/',include('management.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
