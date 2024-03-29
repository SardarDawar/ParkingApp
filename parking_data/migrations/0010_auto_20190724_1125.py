# Generated by Django 2.1.1 on 2019-07-24 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parking_data', '0009_auto_20190723_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking_daily_history',
            name='car_model',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='parking_daily_history',
            name='charged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='parking_daily_history',
            name='end_tm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='parking_daily_history',
            name='reg_num',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='parking_daily_history',
            name='start_tm',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
