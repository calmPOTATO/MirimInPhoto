from django.db import models

class Reservation(models.Model):
    grade = models.CharField(null=False, default="No Grade", max_length=10, verbose_name="학번")
    name = models.CharField(null=False, default="No Name", max_length=10, verbose_name="이름")
    email = models.CharField(null=False, default="No mail", max_length=25, verbose_name="이메일")
    phone = models.CharField(null=False, default="No Number", max_length=15, verbose_name="연락처")
    person = models.IntegerField(null=False, default=0, verbose_name="인원")
    photographer = models.CharField(null=False, default="Not Chose", max_length=10, verbose_name="작가")
    date = models.IntegerField(null=False, default=0)
    date_str = models.CharField(null=False, default="No date", max_length=30)
    check = models.CharField(null=False, default="확정 대기", max_length=10, verbose_name="촬영 여부")
    review_check = models.BooleanField(default=False)


class Review(models.Model):
    name = models.CharField(null=False, default="No Name", max_length=10)
    grade = models.CharField(null=False, default="No Grade", max_length=20)
    title = models.CharField(null=False, default="No email", max_length=25)
    content = models.CharField(null=False, default="No content", max_length = 200)
    date_str = models.CharField(null=False, default="No date", max_length=30)