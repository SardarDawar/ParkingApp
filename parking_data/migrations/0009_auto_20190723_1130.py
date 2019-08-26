# Generated by Django 2.1.1 on 2019-07-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_data', '0008_auto_20190723_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking_slot',
            name='limit',
            field=models.PositiveIntegerField(choices=[(1, '30 min'), (2, '1 hr'), (3, '2 hrs'), (4, '10 sec')], default=1),
        ),
    ]