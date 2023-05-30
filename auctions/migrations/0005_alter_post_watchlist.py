# Generated by Django 4.0.3 on 2023-05-23 15:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_post_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]