from rest_framework import serializers
from .models import IHA,Kategori,KIRALANAN_IHA
from django.contrib.auth.models import User



class IHASerializer(serializers.ModelSerializer):
    kategori_isim = serializers.SerializerMethodField()

    class Meta:
        model = IHA
        fields = '__all__'  

    def get_kategori_isim(self, obj):
        return obj.kategori.isim if obj.kategori else None
    
class UserSerializer(serializers.ModelSerializer):
    kiralanan_iha = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'kiralanan_iha']

    def get_kiralanan_iha(self, obj):
        kiralanan_ihas = KIRALANAN_IHA.objects.filter(user=obj)
        return KIRALANAN_IHASerializer(kiralanan_ihas, many=True, context={'request': self.context.get('request')}).data
    
class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email',  'first_name', 'last_name']

class KIRALANAN_IHASerializer(serializers.ModelSerializer):
    iha = IHASerializer(read_only=True)
    user = SimpleUserSerializer(read_only=True)

    class Meta:
        model = KIRALANAN_IHA
        fields = '__all__'
    
class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'  

    