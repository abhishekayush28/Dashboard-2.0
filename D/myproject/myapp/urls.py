# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get_data/', views.get_data, name='get_data'),
    path('dropdown/', views.dropdown, name='dropdown'),  # Add this line
]
