### İHA Kiralama Projesi

Proje link : https://kambur.net

## Yönetici giriş bilgileri:
email : ihaadmin@example.com  
şifre : IHA123.

## Müşteri giriş bilgileri:
email : test@example.com  
şifre : IHA123.

## Postgresql giriş bilgileri:
Username : iha_db  
Şifre : IHA123.  
Veritabanı Adı: ihadb

## Özellikler:
- Yönetici panelinde; İHA,Kategori,Müşteri ve Kiralık İHA ekleme, listeleme, filtreleme, silme, düzenleme. Kira talebi onaylama veya silme.
- Müşteri panelinde; Kira talebi oluşturma. Kiradaki İHA'ları görüntüleme.
- Yeni müşteri hesabı oluşturma, hesap bilgileri güncelleme, müşteri şifre güncelleme

### Kullanılan yapılar:
Django: REST Framework, Pillow, Serializer, apiview, datetime, Q, messages, User  
JS : Jquery, Ajax


## Önemli işlevler;  
-Tüm listeleme ve filtreleme işlemleri api view ile yapılmıştır.  
-Screen ile zaman mekanizması kurulmuştur.  
-Ön yüzde asenkron fonksiyonlar kullanılmıştır.  
-Ön yüzde Bootstrap kullanılmıştır ayrıca javascript kısmında moment, date-field gibi ekstra kütüphaneler dahil edilmiştir.  
-Proje Linux Ubuntu 20 bir sunucuda kambur.net domaini üzerinde nginx web server ile yapılandırılmıştır.  
-Bağımsız ilişkisel tablolar kullanılmıştır.  