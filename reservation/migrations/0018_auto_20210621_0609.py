# Generated by Django 3.1.7 on 2021-06-20 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0017_auto_20210620_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='email',
            new_name='title',
        ),
    ]