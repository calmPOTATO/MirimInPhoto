# Generated by Django 3.1.7 on 2021-06-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20210617_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='person',
            field=models.IntegerField(default=0, verbose_name='인원'),
        ),
    ]
