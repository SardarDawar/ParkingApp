# Generated by Django 2.1.1 on 2019-07-23 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking_data', '0007_parking_slot_limit_reached'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parking_slot',
            options={'ordering': ('start_tm',)},
        ),
    ]
