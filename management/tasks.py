from celery import shared_task
from .models import IHA , KIRALANAN_IHA
from django.utils import timezone

@shared_task
def delete_expired_ihas():
    now = timezone.now()
    expired_ihas = KIRALANAN_IHA.objects.filter(bitis_tarihi__lte=now)
    for iha in expired_ihas:
        iha.delete()
