# Generated by Django 4.1.3 on 2022-11-02 14:23

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_listing_creation_alter_listing_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.URLField(default='auctions/noimg.jpg'),
        ),
        migrations.AddField(
            model_name='listing',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 14, 23, 27, 411283, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(max_length=1024, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='name',
            field=models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
