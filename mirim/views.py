from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
import getpass
from django.contrib.auth import get_user_model
from reservation import models



def index(request):
    reviews = models.Review.objects.all()
    return render(request, 'mirim/index.html', {'reviews' : reviews})


