# Generated by Django 4.0.8 on 2022-10-31 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widecity_shopping', '0003_wallet_history_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet_history',
            name='Debit_Credit',
            field=models.CharField(default='credited', max_length=500),
        ),
    ]