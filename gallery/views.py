from django.shortcuts import render
from gallery.models import Photo
from django.contrib.auth import get_user_model


def gallery(request):
    return render(request, 'gallery/gallery.html')

def photographer(request):
    return render(request, 'gallery/photographer.html')

def project(request):
    return render(request, 'gallery/project.html')

def profile(request):
    return render(request, 'gallery/gallery_photographer_profile.html')





def Entrance(request):
    photos = Photo.objects.filter(title="location", sub_title="entrance")
    return render(request, 'gallery/gallery_location_Entrance.html', {'photos': photos})

def BackSide(request):
    photos = Photo.objects.filter(title="location", sub_title="backside")
    return render(request, 'gallery/gallery_location_BackSide.html', {'photos': photos})

def Garden(request):
    photos = Photo.objects.filter(title="location", sub_title="garden")
    return render(request, 'gallery/gallery_location_Garden.html', {'photos': photos})

def Indoor(request):
    photos = Photo.objects.filter(title="location", sub_title="indoor")
    return render(request, 'gallery/gallery_location_Indoor.html', {'photos': photos})

def Roof(request):
    photos = Photo.objects.filter(title="location", sub_title="root")
    return render(request, 'gallery/gallery_location_Roof.html', {'photos': photos})





def bada(request):
    photos = Photo.objects.filter(title="photographer", sub_title="김바다")
    return render(request, 'gallery/gallery_photographer_1.html', {'photos': photos})

def jeongmi(request):
    photos = Photo.objects.filter(title="photographer", sub_title="김정미")
    return render(request, 'gallery/gallery_photographer_2.html', {'photos': photos})

def seeun(request):
    photos = Photo.objects.filter(title="photographer", sub_title="안세은")
    return render(request, 'gallery/gallery_photographer_3.html', {'photos': photos})

def dayeon(request):
    photos = Photo.objects.filter(title="photographer", sub_title="양다연")
    return render(request, 'gallery/gallery_photographer_4.html', {'photos': photos})

def yeyoung(request):
    photos = Photo.objects.filter(title="photographer", sub_title="유예영")
    return render(request, 'gallery/gallery_photographer_5.html', {'photos': photos})

def seoyeon(request):
    photos = Photo.objects.filter(title="photographer", sub_title="이서연")
    return render(request, 'gallery/gallery_photographer_6.html', {'photos': photos})

def yeseo(request):
    photos = Photo.objects.filter(title="photographer", sub_title="예서")
    return render(request, 'gallery/gallery_photographer_7.html', {'photos': photos})

def minseo(request):
    photos = Photo.objects.filter(title="photographer", sub_title="민서")
    return render(request, 'gallery/gallery_photographer_8.html', {'photos': photos})

def sael(request):
    photos = Photo.objects.filter(title="photographer", sub_title="하사엘")
    return render(request, 'gallery/gallery_photographer_9.html', {'photos': photos})

def narae(request):
    photos = Photo.objects.filter(title="photographer", sub_title="한나래")
    return render(request, 'gallery/gallery_photographer_10.html', {'photos': photos})

def haewon(request):
    photos = Photo.objects.filter(title="photographer", sub_title="전해원")
    return render(request, 'gallery/gallery_photographer_11.html', {'photos': photos})

def seoyoung(request):
    photos = Photo.objects.filter(title="photographer", sub_title="장서영")
    return render(request, 'gallery/gallery_photographer_12.html', {'photos': photos})

def jinmin(request):
    photos = Photo.objects.filter(title="photographer", sub_title="성진민")
    return render(request, 'gallery/gallery_photographer_13.html', {'photos': photos})

def jinhee(request):
    photos = Photo.objects.filter(title="photographer", sub_title="주진희")
    return render(request, 'gallery/gallery_photographer_14.html', {'photos': photos})




def project(request):
    return render(request, 'gallery/gallery_project_slider.html')

def project1(request):
    photos = Photo.objects.filter(title="project", sub_title="project_1")
    return render(request, 'gallery/gallery_project_1.html', {'photos':photos})

def project2(request):
    photos = Photo.objects.filter(title="project", sub_title="project_2")
    return render(request, 'gallery/gallery_project_2.html', {'photos':photos})

def project3(request):
    photos = Photo.objects.filter(title="project", sub_title="project_3")
    return render(request, 'gallery/gallery_project_3.html', {'photos': photos})

def project4(request):
    photos = Photo.objects.filter(title="project", sub_title="project_4")
    return render(request, 'gallery/gallery_project_4.html', {'photos': photos})

def project5(request):
    photos = Photo.objects.filter(title="project", sub_title="project_5")
    return render(request, 'gallery/gallery_project_5.html', {'photos': photos})

def project6(request):
    photos = Photo.objects.filter(title="project", sub_title="project_6")
    return render(request, 'gallery/gallery_project_6.html', {'photos': photos})

def project7(request):
    photos = Photo.objects.filter(title="project", sub_title="project_7")
    return render(request, 'gallery/gallery_project_7.html', {'photos': photos})

def project8(request):
    photos = Photo.objects.filter(title="project", sub_title="project_8")
    return render(request, 'gallery/gallery_project_8.html', {'photos': photos})

def project9(request):
    photos = Photo.objects.filter(title="project", sub_title="project_9")
    return render(request, 'gallery/gallery_project_9.html', {'photos': photos})
