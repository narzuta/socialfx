# Generated by Django 2.0.5 on 2018-05-16 18:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_header',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/upload'),
        ),
    ]
