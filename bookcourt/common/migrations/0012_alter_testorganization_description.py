# Generated by Django 3.2.20 on 2023-08-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_auto_20230821_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testorganization',
            name='description',
            field=models.TextField(default='No Description set'),
        ),
    ]