from django.urls import path
from . import views

app_name = 'birthday_show'

urlpatterns = [
    path('', views.index, name='index'),
] 