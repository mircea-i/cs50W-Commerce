# Generated by Django 4.0.6 on 2022-11-07 14:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_rename_starting_bid_listing_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 14, 14, 32, 593198, tzinfo=utc)),
        ),
    ]