# Generated by Django 3.0.4 on 2020-03-20 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraper_app', '0004_auto_20200320_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='source',
            new_name='url',
        ),
    ]
