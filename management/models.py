from django.db import models
from django.contrib.auth.models import User

class Kategori(models.Model):
    isim = models.CharField(max_length=100)
    tanim = models.CharField(max_length=100)


class IHA(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    agirlik = models.FloatField()
    ucus_suresi = models.IntegerField()  
    menzil = models.IntegerField() 
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE , null=True , blank=True)
    yuk_kapasitesi = models.FloatField()
    navigasyon = models.CharField(default=False , null=True , blank=True)
    oto_pilot = models.CharField(default=False, null=True , blank=True)
    maksimum_hiz = models.FloatField() 
    eklenme_tarihi = models.DateTimeField(auto_now_add = True , null = True , blank = True)
    resim = models.ImageField(upload_to='iha_resimleri/', null=True, blank=True)
    status = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.marka} {self.model}"

class KIRALANAN_IHA(models.Model):
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE , null=True , blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    baslangic_tarihi = models.DateTimeField()
    bitis_tarihi = models.DateTimeField()
    status = models.CharField(max_length=100)




    