from django.urls import path
from . import views,hire

app_name = 'panel' 

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('home', views.home, name='home'),
    path('login' , views.login_user , name='login' ),
    path('register' , views.register_user , name='register' ),
    path('logout' , views.logout_user , name='logout' ),
    path('hire' , hire.index , name='hire' ),
    path('rented-iha' , hire.rented_iha , name='rented-iha' ),
    path('account' , views.account , name='account' ),
    path('password_change' , views.password_change , name='password_change' )
    
]
