# Generated by Django 4.0.3 on 2023-05-30 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auctionlisting_closed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
    ]