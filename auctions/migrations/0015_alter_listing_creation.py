# Generated by Django 4.0.6 on 2022-11-07 14:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_listing_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 14, 15, 16, 643018, tzinfo=utc)),
        ),
    ]