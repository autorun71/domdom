# Generated by Django 2.1.5 on 2019-01-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domapp', '0004_remove_categories_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=100)),
            ],
        ),
    ]
