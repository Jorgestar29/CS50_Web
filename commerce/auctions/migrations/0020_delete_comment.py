# Generated by Django 3.0.8 on 2020-08-13 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_bid_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
