from django.urls import path
from . import views,iha
from panel import views as grep

app_name = 'management' 

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create-iha', iha.create, name='create-iha'),
    path('list-iha', iha.list, name='list-iha'),
    path('api/kategori/', iha.kategori_list, name='kategori-list'),
    path('create-category', iha.create_category, name='create-category'),
    path('delete-category/<int:id>', iha.kategori_sil, name='delete-category'),
    path('edit-category/<int:id>', iha.edit_category, name='edit-category'),
    path('hire-list', iha.kiralanan_list, name='hire-list'),
    path('user-list', iha.user_list_, name='user-list'),
    path('user-sil/<int:id>', iha.user_sil, name='user-sil'),
    path('category-list', iha.kategori_list_view, name='category-list'),
    path('api/iha/', iha.iha_list, name='iha-list'),
    path('api/user-list/', iha.user_list, name='api-user-list'),
    path('api/hire-iha/', iha.kiralanan_iha_list, name='hire-iha'),
    path('iha_sil/<int:id>' , iha.iha_sil , name="iha_sil"),
    path('edit_iha/<int:id>' , iha.iha_duzenle , name="iha_duzenle"),
    path('account' , grep.account , name = "account"),
    path('password_change' , grep.password_change , name = "password_change"),
    path('iha-kiralama' , iha.iha_kiralama , name = "iha-kiralama"),
    path('kiralanan-iha-sil/<int:id>' , iha.kiralanan_iha_sil , name = "kiralanan-iha-sil"),
    path('kiralanan-iha-onay/<int:id>' , iha.kiralanan_iha_onay , name = "kiralanan_iha_onay")
]
