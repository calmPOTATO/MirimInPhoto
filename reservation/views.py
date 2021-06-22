import allauth.account.utils
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from reservation.models import Reservation, Review
import datetime
from django.contrib.auth import get_user_model
import json

#예약 현황
def reservationList(request):
    if(request.GET.get('photographer')):
        name = request.GET.get('photographer')
        photographer = Reservation.objects.filter(photographer=name)

        p_list = []

        for p in photographer:
            year = str(p.date)[0:4]
            month = str(p.date)[4:6]
            day = str(p.date)[6:8]
            date = year+"/"+month+"/"+day
            p_list.append(date)

        return render(request, 'reservation/Calendar.html', {'p_list' : p_list})
    else:
        return render(request, 'reservation/Calendar.html')

#예약
def individual(request):
    return render(request, 'reservation/reservation_individual.html')

#그룹예약
def group(request):
    return render(request, 'reservation/reservation_group.html')

#내 예약 현황
def myPage(request):
    User = request.user
    reservations = Reservation.objects.filter(name=User.first_name).order_by('-date')
    return render(request, 'reservation/my_reservation.html', {'indiv': reservations})

#리뷰달러가기
def review(request):
    User = request.user
    reservations = Reservation.objects.filter(name=User.first_name, review_check=False, check="촬영 완료").order_by('-date')
    return render(request, 'reservation/reservation_review.html', {'reservations': reservations})

#리뷰값 DB에 Insert
def insertReview(request):
    User = request.user
    username = User.first_name
    grade = User.last_name
    date = request.POST['date'];
    title = request.POST['title'];
    content = request.POST['content'];


    
    #DB에 리뷰 넣는 코드 작성
    newreview = Review(name=username, grade=grade, date_str=date, title=title, content=content)
    newreview.save()
    #review_check true로 바꾸기
    t_reservation = Reservation.objects.filter(name=username, date_str=date)
    t_reservation.update(review_check=True)


    return HttpResponseRedirect('/reservation/my_page')


#예약 취소
def delReservation(request, date):
    User = request.user
    Reservation.objects.filter(name=User.first_name, date=date).delete();
    reservations = Reservation.objects.filter(name=User.first_name).order_by('date_str')
    return render(request, 'reservation/my_reservation.html', {'indiv': reservations})

#개인 예약 DB에 넣는 함수
def insertIndivid(request):
    grade = request.POST['grade']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    photographer = request.POST['photo_g']
    date = int(request.POST['date'])
    date_string = request.POST['date']
    date_str = date_string[0:4]+"년 "+date_string[4:6]+"월 "+date_string[6:8]+"일"



    qs = Reservation(grade=grade, name=name, email=email, phone=phone, person=1, photographer=photographer, date=date, date_str=date_str)
    qs.save()
    return HttpResponseRedirect(reverse('reservation:my_page'))

#그룹 예약 DB에 넣는 함수
def insertGroup(request):
    grade = request.POST['grade']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    person = request.POST['person']
    photographer = request.POST['photo_g']
    date = int(request.POST['date'])
    date_string = request.POST['date']
    date_str = date_string[0:4] + "년 " + date_string[4:6] + "월 " + date_string[6:8] + "일"

    qs = Reservation(grade=grade, name=name, email=email, phone=phone, person=person, photographer=photographer, date=date, date_str=date_str)
    qs.save()

    return HttpResponseRedirect(reverse('reservation:my_page'))
