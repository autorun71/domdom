# Generated by Django 2.1.5 on 2019-01-18 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domapp', '0003_auto_20190118_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='date',
        ),
    ]
