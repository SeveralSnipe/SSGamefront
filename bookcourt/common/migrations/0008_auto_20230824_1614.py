# Generated by Django 3.2.20 on 2023-08-24 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20230824_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationlocation',
            name='area_name',
        ),
        migrations.RemoveField(
            model_name='organizationlocation',
            name='city_name',
        ),
        migrations.RemoveField(
            model_name='organizationlocation',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='organizationlocation',
            name='state_name',
        ),
        migrations.AddField(
            model_name='organizationlocation',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='common.area'),
        ),
    ]
