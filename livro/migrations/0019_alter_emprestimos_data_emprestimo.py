# Generated by Django 3.2.23 on 2023-11-23 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0018_auto_20211028_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 23, 14, 7, 52, 595249)),
        ),
    ]
