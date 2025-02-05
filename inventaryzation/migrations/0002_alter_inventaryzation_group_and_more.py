# Generated by Django 4.2.2 on 2024-12-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaryzation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventaryzation',
            name='group',
            field=models.CharField(choices=[('---', '---'), ('Автомобілі', 'Автомобілі'), ('Меблі', 'Меблі'), ('Будівлі', 'Будівлі'), ('Орг.техніка', 'Орг.техніка'), ('Периферія', 'Периферія'), ('Ноутбуки та ПК', 'Ноутбуки та ПК'), ('Смартфони та планшети', 'Смартфони та планшети'), ('Складське обладнання', 'Складське обладнання'), ('Предмети інтерєру', 'Предмети інтерєру'), ('Мережеве обладнання', 'Мережеве обладнання')], default='---', max_length=100),
        ),
        migrations.AlterField(
            model_name='inventaryzation',
            name='market_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='inventaryzation',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
