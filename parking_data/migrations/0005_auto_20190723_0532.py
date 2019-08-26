# Generated by Django 2.1.1 on 2019-07-23 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_data', '0004_auto_20190722_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parking_slot',
            name='update_tm',
        ),
        migrations.AddField(
            model_name='parking_slot',
            name='updated_tm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='parking_slot',
            name='start_tm',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]