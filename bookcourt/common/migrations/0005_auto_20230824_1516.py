# Generated by Django 3.2.20 on 2023-08-24 09:46

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20230824_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationlocation',
            name='area',
        ),
        migrations.AddField(
            model_name='organizationlocation',
            name='area_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='area_name', chained_model_field='area_name', default='', on_delete=django.db.models.deletion.CASCADE, to='common.area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationlocation',
            name='city_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='city_name', chained_model_field='city_name', default='', on_delete=django.db.models.deletion.CASCADE, to='common.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationlocation',
            name='country_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='common.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizationlocation',
            name='state_name',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='country_name', chained_model_field='country_name', default=None, on_delete=django.db.models.deletion.CASCADE, to='common.state'),
            preserve_default=False,
        ),
    ]
