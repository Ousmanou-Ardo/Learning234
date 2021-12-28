from django.urls import path
from . import views

app_name = 'moic'
urlpatterns = [
path('', views.index, name='index'),
]