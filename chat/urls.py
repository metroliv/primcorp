from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chat_index'),  # Chat page view
]
