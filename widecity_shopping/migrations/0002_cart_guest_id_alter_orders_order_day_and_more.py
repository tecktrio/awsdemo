# Generated by Django 4.0.8 on 2022-11-09 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widecity_shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='guest_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Order_day',
            field=models.IntegerField(default=9),
        ),
        migrations.AlterField(
            model_name='products',
            name='manufacturing_date',
            field=models.CharField(default=datetime.date(2022, 11, 9), max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='signup_day',
            field=models.CharField(default=9, max_length=50),
        ),
    ]
