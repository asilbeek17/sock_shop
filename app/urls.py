from django.urls import path

from app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('contact/', contact, name='contact'),
    path('testmonial/', testmonial, name='testmonial'),
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
]
