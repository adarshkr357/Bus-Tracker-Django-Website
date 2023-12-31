# Generated by Django 4.2.5 on 2023-09-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('bus_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('bus_name', models.CharField(max_length=50)),
                ('driver_id', models.IntegerField(unique=True)),
                ('driver_username', models.CharField(max_length=50)),
                ('driver_email', models.EmailField(max_length=254)),
                ('driver_password', models.CharField(max_length=254)),
                ('driver_name', models.CharField(max_length=50)),
                ('bus_route', models.CharField(max_length=255)),
                ('latest_stop_name', models.CharField(blank=True, max_length=50, null=True)),
                ('fare', models.CharField(max_length=255)),
                ('emission_compliance', models.CharField(blank=True, max_length=50, null=True)),
                ('fuel_type', models.CharField(max_length=50)),
                ('current_latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('current_longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('last_login', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=254)),
                ('current_bus_id', models.CharField(blank=True, max_length=50, null=True)),
                ('current_fare', models.IntegerField(blank=True, null=True)),
                ('current_latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('current_longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('last_login', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
