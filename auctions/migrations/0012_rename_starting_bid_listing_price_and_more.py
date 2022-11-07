# Generated by Django 4.0.6 on 2022-11-07 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_comment_listing_alter_listing_creation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='starting_bid',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='listing',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 12, 4, 44, 611993, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
