# Generated by Django 3.2.20 on 2023-08-24 09:57

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_auto_20230824_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationlocation',
            name='area_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='city_name', chained_model_field='city', null=True, on_delete=django.db.models.deletion.CASCADE, to='common.area'),
        ),
        migrations.AlterField(
            model_name='organizationlocation',
            name='city_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='state_name', chained_model_field='state', null=True, on_delete=django.db.models.deletion.CASCADE, to='common.city'),
        ),
    ]
