# Generated by Django 4.2.2 on 2024-10-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0018_alter_inventaryzation_date_of_purchase_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='xlsfile/')),
            ],
        ),
    ]
