# Generated by Django 3.2.20 on 2023-08-22 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_testorganization_organization_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testorganization',
            name='organization_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
