from django.urls import path 
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('profile', views.profile , name = 'profile'),
    path('cart', views.cart , name = 'cart'),
    path('checkout', views.checkout , name = 'checkout'),
    path('contact/' , views.contact , name = 'contact'),

    path('user_register' , views.UserRegisterView , name = 'UserRegister'),
    path('profile_register/<str:user_pk>' , views.ProfileRegisterView , name = 'ProfileRegister'),
    path('login/' , views.loginView , name = 'login'),
    path('logout/' , views.logoutView , name = 'logout'),

    path('password_reset/' , auth_views.PasswordResetView.as_view(template_name="main/reset_pass.html") , name = 'password_reset'),
    path('password_reset_done/' , auth_views.PasswordResetDoneView.as_view(template_name="main/reset_pass_done.html") , name = 'password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>' , auth_views.PasswordResetConfirmView.as_view() , name = 'password_reset_confirm'),
    path('password_reset_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name="main/reset_pass_complete.html") , name = 'password_reset_complete'),

    path('update-cart/' , views.updateCart , name = 'update-cart'),

]