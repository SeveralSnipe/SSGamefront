# Generated by Django 3.2.20 on 2023-08-24 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20230824_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationlocation',
            name='area',
        ),
    ]
