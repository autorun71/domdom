# Generated by Django 2.1.5 on 2019-01-18 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domapp', '0002_auto_20190118_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 1, 18, 19, 38, 21, 503971)),
        ),
    ]
