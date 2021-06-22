from django.db import models
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.templatetags.static import static
from django.conf.urls.static import static
from django.conf import settings


class Photo(models.Model) :
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    img_num = models.IntegerField(null=False, default=0)
    photo_width = models.IntegerField(blank=True, null=True)
    photo_height = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/')

#이미지 사이즈 조절, 워터마크 넣는 기능
# sender(UploadPhoto)
@receiver(post_save, sender=Photo)
def overlay_watermark(instance, sender, **kwargs):
    photo = Image.open(instance.photo)
    width = instance.photo_width
    height = instance.photo_height
    print(width, height)
    watermark = Image.open("gallery/static/img/watermark.png")
    watermark = watermark.resize((150, 50), Image.ANTIALIAS)

    photo = photo.resize((width, height), Image.ANTIALIAS)
    photo.paste(watermark, (width-150, height-50), watermark)
    photo.save(instance.photo.path)

