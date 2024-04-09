
from django.urls import path
from .views import store_lab_data

urlpatterns = [
    path('store-lab-data/', store_lab_data, name='store_lab_data'),
]
