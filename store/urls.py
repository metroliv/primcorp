from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.all_services, name='all_services'),
    # Add more URLs if needed, such as for adding a custom system or contact us page
    path('add_custom_system/', views.add_custom_system, name='add_custom_system'),  # Example for adding a custom system
    path('contact_us/', views.contact_us, name='contact_us'),  # Example for a contact us page
]
