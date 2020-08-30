# Generated by Django 3.0.7 on 2020-08-26 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0004_presence_isparticular'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presence',
            name='isParticular',
        ),
        migrations.AlterField(
            model_name='presence',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='call of roll date'),
        ),
        migrations.AlterField(
            model_name='presence',
            name='reason',
            field=models.CharField(max_length=255, null=True),
        ),
    ]