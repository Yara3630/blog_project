from django.urls import path
from .views import about, technology


app_name = 'about'

urlpatterns = [
    path('', about, name='about'),
    path('technology/', technology, name='technology'),
]
