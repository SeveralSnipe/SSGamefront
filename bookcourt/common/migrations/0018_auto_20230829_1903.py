# Generated by Django 3.2.20 on 2023-08-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_auto_20230829_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationlocationworkingtime',
            name='from_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizationlocationworkingtime',
            name='to_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]