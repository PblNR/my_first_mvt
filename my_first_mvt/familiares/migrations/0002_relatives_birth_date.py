# Generated by Django 4.0.6 on 2022-07-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatives',
            name='birth_date',
            field=models.DateField(default='1950-10-10'),
        ),
    ]
