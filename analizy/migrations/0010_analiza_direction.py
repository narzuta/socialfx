# Generated by Django 2.1a1 on 2018-06-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analizy', '0009_auto_20180603_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='analiza',
            name='direction',
            field=models.CharField(choices=[('NEUTRAL', 'NEUTRAL'), ('SELL', 'SELL'), ('BUY', 'BUY')], default='NEUTRAL', max_length=200),
        ),
    ]
