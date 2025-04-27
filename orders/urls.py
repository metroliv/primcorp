from django.urls import path
from . import views

urlpatterns = [
    path('order/<int:system_id>/', views.order_system, name='order_system'),
    path('order_service/<int:id>/', views.order_service, name='order_service'),
    path('order/confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]
