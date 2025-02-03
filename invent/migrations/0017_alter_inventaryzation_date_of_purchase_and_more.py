# Generated by Django 4.2.2 on 2024-10-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0016_alter_inventaryzation_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventaryzation',
            name='date_of_purchase',
            field=models.DateField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='inventaryzation',
            name='date_of_registration',
            field=models.DateField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='inventaryzation',
            name='group',
            field=models.CharField(choices=[('---', '---'), ('Автомобілі', 'Автомобілі'), ('Меблі', 'Меблі'), ('Будівлі', 'Будівлі'), ('Орг.техніка', 'Орг.техніка'), ('Периферія', 'Периферія'), ("Ноутбуки та комп'ютери", "Ноутбуки та комп'ютери"), ('Смартфони та планшети', 'Смартфони та планшети'), ('Складське обладнання', 'Складське обладнання'), ('Предмети інтерєру', 'Предмети інтерєру')], default='---', max_length=100),
        ),
    ]
