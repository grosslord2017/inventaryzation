# Generated by Django 4.2.2 on 2024-10-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0020_remove_downloadfiles_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DownloadFiles',
        ),
        migrations.AlterField(
            model_name='inventaryzation',
            name='group',
            field=models.CharField(choices=[('---', '---'), ('Автомобілі', 'Автомобілі'), ('Меблі', 'Меблі'), ('Будівлі', 'Будівлі'), ('Орг.техніка', 'Орг.техніка'), ('Периферія', 'Периферія'), ('Ноутбуки та ПК', 'Ноутбуки та ПК'), ('Смартфони та планшети', 'Смартфони та планшети'), ('Складське обладнання', 'Складське обладнання'), ('Предмети інтерєру', 'Предмети інтерєру')], default='---', max_length=100),
        ),
    ]
