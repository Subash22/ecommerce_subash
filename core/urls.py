from django.urls import path
from .views import index, cart, removecart, error_page, success_page

urlpatterns = [
    path('', index),
    path('cart/', cart),
    path('cart/remove/<int:id>', removecart),
    path('success_page/', success_page, name="success_page"),
    path('error_page/', error_page, name="error_page"),
]
