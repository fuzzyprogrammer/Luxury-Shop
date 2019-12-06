from django.urls import path

from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('',views.index,name='home'),
]
