# Generated by Django 4.2.2 on 2023-10-31 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0008_alter_item_is_decommissioned_alter_item_is_reserve_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='marker',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]