# Generated by Django 4.2.2 on 2025-01-08 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventaryzation', '0006_jurnal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jurnal',
            old_name='date_oeration',
            new_name='date_operation',
        ),
    ]
