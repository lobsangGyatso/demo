# Generated by Django 2.1.7 on 2019-11-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_auto_20191129_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='econtact',
            field=models.IntegerField(),
        ),
    ]
