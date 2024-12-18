# Generated by Django 5.1.2 on 2024-11-22 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0002_alter_car_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestDriveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.car')),
            ],
        ),
    ]
