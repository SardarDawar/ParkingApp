# Generated by Django 2.1.1 on 2019-07-23 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_data', '0006_auto_20190723_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking_slot',
            name='limit_reached',
            field=models.BooleanField(default=False),
        ),
    ]
