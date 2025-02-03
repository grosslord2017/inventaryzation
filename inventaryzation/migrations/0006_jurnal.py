# Generated by Django 4.2.2 on 2025-01-08 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaryzation', '0005_rename_archive_archiveutil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurnal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[("Додавання об'єкта", "Додавання об'єкта"), ('Списання', 'Списання'), ('Зміна МВО', 'Зміна МВО')], max_length=100)),
                ('from_whom', models.CharField(max_length=100)),
                ('to_whom', models.CharField(max_length=100)),
                ('item', models.TextField()),
                ('reason', models.TextField()),
                ('date_oeration', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
