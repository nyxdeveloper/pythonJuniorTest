# Generated by Django 3.0.7 on 2020-11-24 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201124_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='failed',
            field=models.BooleanField(default=False, verbose_name='Провалено'),
        ),
        migrations.AddField(
            model_name='todo',
            name='lastDay',
            field=models.BooleanField(default=False, verbose_name='Последний день'),
        ),
    ]
