# Generated by Django 2.1.7 on 2019-11-30 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_auto_20191130_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
    ]
