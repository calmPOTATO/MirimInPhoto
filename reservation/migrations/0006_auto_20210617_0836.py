# Generated by Django 3.1.7 on 2021-06-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_auto_20210616_2352'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='individual',
            name='person',
            field=models.IntegerField(default=1, verbose_name='인원'),
        ),
    ]
