# Generated by Django 2.1.5 on 2019-01-18 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domapp', '0007_auto_20190118_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
    ]
