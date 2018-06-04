# Generated by Django 2.1a1 on 2018-06-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analizy', '0002_analiza_waluta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analiza',
            name='waluta',
        ),
        migrations.AddField(
            model_name='analiza',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]