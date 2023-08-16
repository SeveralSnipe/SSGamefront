# Generated by Django 3.2.20 on 2023-08-10 10:54

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('organization_name', models.CharField(max_length=100)),
                ('alt_number', models.PositiveBigIntegerField()),
                ('description', models.TextField()),
                ('is_terms_and_conditions_agreed', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(1, 'Approved'), (2, 'Pending'), (3, 'In Progress'), (4, 'Cancelled')], default=2)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.TextField(max_length=255)),
                ('address_line_2', models.TextField(max_length=255)),
                ('area', models.TextField(max_length=50)),
                ('city', models.TextField(max_length=50)),
                ('state', models.TextField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('contact_number', models.PositiveBigIntegerField()),
                ('work_from_time', models.DateTimeField()),
                ('work_to_time', models.DateTimeField()),
                ('join_date', models.DateField()),
                ('created_date', models.DateField(auto_now=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sign_up_terms_and_conditions', models.TextField()),
                ('booking_terms_and_conditions', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationLocationWorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_monday_workingday', models.BooleanField(default=True)),
                ('is_tuesday_workingday', models.BooleanField(default=True)),
                ('is_wednesday_workingday', models.BooleanField(default=True)),
                ('is_thursday_workingday', models.BooleanField(default=True)),
                ('is_friday_workingday', models.BooleanField(default=True)),
                ('is_saturday_workingday', models.BooleanField(default=True)),
                ('is_sunday_workingday', models.BooleanField(default=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.organizationlocation')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationLocationGameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_calculate_timing', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('game_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.gametype')),
                ('organization_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.organizationlocation')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationGameImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.organizationlocationgametype')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_parking', models.BooleanField(default=False)),
                ('is_restrooms', models.BooleanField(default=False)),
                ('is_changerooms', models.BooleanField(default=False)),
                ('is_powerbackup', models.BooleanField(default=False)),
                ('is_beverages_facility', models.BooleanField(default=False)),
                ('is_coaching_facilities', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.organizationlocation')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.tenant'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.tenant')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
