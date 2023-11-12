from django.urls import path

from .views import contacts, home

app_name = 'catalog_list'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
