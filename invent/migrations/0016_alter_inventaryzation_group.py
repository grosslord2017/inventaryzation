# Generated by Django 4.2.2 on 2024-10-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0015_alter_inventaryzation_date_of_purchase_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventaryzation',
            name='group',
            field=models.CharField(choices=[('0', '---'), ('1', 'Автомобілі'), ('2', 'Меблі'), ('3', 'Будівлі'), ('4', 'Орг.техніка'), ('5', 'Периферія'), ('6', "Ноутбуки та комп'ютери"), ('7', 'Смартфони та планшети'), ('8', 'Складське обладнання'), ('9', 'Предмети інтерєру')], default='---', max_length=100),
        ),
    ]