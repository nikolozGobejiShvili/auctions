# Generated by Django 4.0.3 on 2023-05-30 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_rename_body_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]