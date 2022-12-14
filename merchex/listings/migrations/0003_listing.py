# Generated by Django 4.0.6 on 2022-08-02 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('RC', 'Records'), ('CL', 'Clothing'), ('PT', 'Posters'), ('MC', 'Miscellaneous')], max_length=10)),
                ('description', models.CharField(max_length=250)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2022)])),
                ('sold', models.BooleanField(default=True)),
            ],
        ),
    ]
