# Generated by Django 2.1.1 on 2019-07-22 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parking_slot',
            name='current_tm',
        ),
    ]
