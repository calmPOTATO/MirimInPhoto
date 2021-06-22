from django.contrib import admin
from .models import Reservation, Review


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['grade', 'name', 'email', 'phone', 'photographer', 'date', 'check']


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Review)
