# Generated by Django 2.0.5 on 2018-05-16 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180516_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_header',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='blog/media/upload'),
        ),
    ]
