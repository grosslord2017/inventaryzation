# Generated by Django 4.2.2 on 2024-12-23 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaryzation', '0003_alter_inventaryzation_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=100)),
                ('name_model', models.CharField(max_length=100)),
                ('serial', models.CharField(max_length=100)),
                ('inv_numb', models.CharField(max_length=100)),
                ('responsible', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField(default=0.0)),
                ('reason_for_disposal', models.TextField()),
                ('date_of_registration', models.DateField()),
                ('date_of_utilization', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
