from django.urls import path, include
from . import views

app_name = 'mirim'

urlpatterns = [
    path('', views.index, name='index'),

]
