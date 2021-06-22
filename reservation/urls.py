from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.reservationList, name='list'),
    path('individual/', views.individual, name='individual'),
    path('group/', views.group, name='group'),
    path('my_page/', views.myPage, name='my_page'),
    path('review/', views.review, name="review"),

    path('insertReview/', views.insertReview, name='insertReview'),
    path('delReservation/<int:date>', views.delReservation, name='delReservation'),
    path('insertI/', views.insertIndivid, name='insertIndivid'),
    path('insertG/', views.insertGroup, name='insertGroup'),

]
