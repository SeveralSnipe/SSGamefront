# Generated by Django 3.2.20 on 2023-08-21 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('common', '0009_alter_organizationlocationworkingdays_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestOrganization',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='auth.user')),
                ('organization_name', models.CharField(max_length=100)),
                ('alt_number', models.PositiveBigIntegerField()),
                ('description', models.TextField()),
                ('is_terms_and_conditions_agreed', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(1, 'Approved'), (2, 'Pending'), (3, 'In Progress'), (4, 'Cancelled')], default=2)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TestOrganizationLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.TextField(max_length=255)),
                ('address_line_2', models.TextField(max_length=255)),
                ('area', models.TextField(max_length=50)),
                ('city', models.TextField(max_length=50)),
                ('state', models.TextField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('contact_number', models.PositiveBigIntegerField()),
                ('join_date', models.DateField()),
                ('created_date', models.DateField(auto_now=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.testorganization')),
            ],
        ),
        migrations.CreateModel(
            name='TestOrganizationLocationWorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_monday_workingday', models.BooleanField(default=True)),
                ('is_tuesday_workingday', models.BooleanField(default=True)),
                ('is_wednesday_workingday', models.BooleanField(default=True)),
                ('is_thursday_workingday', models.BooleanField(default=True)),
                ('is_friday_workingday', models.BooleanField(default=True)),
                ('is_saturday_workingday', models.BooleanField(default=True)),
                ('is_sunday_workingday', models.BooleanField(default=True)),
                ('organization', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='common.testorganizationlocation')),
            ],
        ),
        migrations.CreateModel(
            name='TestOrganizationLocationGameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('game_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.gametype')),
                ('organization_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.testorganizationlocation')),
            ],
        ),
        migrations.CreateModel(
            name='TestOrganizationLocationAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_parking', models.BooleanField(default=False)),
                ('is_restrooms', models.BooleanField(default=False)),
                ('is_changerooms', models.BooleanField(default=False)),
                ('is_powerbackup', models.BooleanField(default=False)),
                ('is_beverages_facility', models.BooleanField(default=False)),
                ('is_coaching_facilities', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('organization_location', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='common.testorganizationlocation')),
            ],
        ),
        migrations.CreateModel(
            name='TestLocationCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TestLocationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.testlocationcity')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TestCustomer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='auth.user')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='common.tenant')),
            ],
        ),
    ]