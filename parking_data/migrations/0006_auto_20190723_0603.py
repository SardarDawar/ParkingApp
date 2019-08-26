# Generated by Django 2.1.1 on 2019-07-23 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_data', '0005_auto_20190723_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parking_slot',
            name='occupied',
        ),
        migrations.AddField(
            model_name='parking_slot',
            name='charged',
            field=models.BooleanField(default=False),
        ),
    ]
