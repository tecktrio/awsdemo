# Generated by Django 4.0.8 on 2022-11-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widecity_shopping', '0006_alter_products_image_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='arrival_date',
            new_name='manufacturing_date',
        ),
        migrations.RemoveField(
            model_name='products',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='orders',
            name='Order_day',
            field=models.CharField(default=3, max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='signup_day',
            field=models.CharField(default=3, max_length=50),
        ),
    ]
