# Generated by Django 3.1.7 on 2021-06-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('photo_width', models.IntegerField(blank=True, null=True)),
                ('photo_height', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
