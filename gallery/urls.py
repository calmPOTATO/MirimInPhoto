from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery, name='gall_index'),

    path('location/Entrance/', views.Entrance, name='entrance'),
    path('location/BackSide/', views.BackSide, name='backside'),
    path('location/Garden/', views.Garden, name='garden'),
    path('location/Indoor/', views.Indoor, name='indoor'),
    path('location/Roof/', views.Roof, name='roof'),

    path('photographer/profile/', views.profile, name='profile'),
    path('photographer/bada/', views.bada, name='bada'),
    path('photographer/jeongmi/', views.jeongmi, name='jeongmi'),
    path('photographer/seeun/', views.seeun, name='seeun'),
    path('photographer/dayeon/', views.dayeon, name='dayeon'),
    path('photographer/yeyoung/', views.yeyoung, name='yeyoung'),
    path('photographer/seoyeon/', views.seoyeon, name='seoyeon'),
    path('photographer/yeseo/', views.yeseo, name='yeseo'),
    path('photographer/minseo/', views.minseo, name='minseo'),
    path('photographer/sael/', views.sael, name='sael'),
    path('photographer/narae/', views.narae, name='narae'),
    path('photographer/haewon/', views.haewon, name='haewon'),
    path('photographer/seoyoung/', views.seoyoung, name='seoyoung'),
    path('photographer/jinmin/', views.jinmin, name='jinmin'),
    path('photographer/jinhee/', views.jinhee, name='jinhee'),

    path('project/main/', views.project, name="project"),
    path('project/1/', views.project1, name='project1'),
    path('project/2/', views.project2, name='project2'),
    path('project/3/', views.project3, name='project3'),
    path('project/4/', views.project4, name='project4'),
    path('project/5/', views.project5, name='project5'),
    path('project/6/', views.project6, name='project6'),
    path('project/7/', views.project7, name='project7'),
    path('project/8/', views.project8, name='project8'),
    path('project/9/', views.project9, name='project9'),



]
