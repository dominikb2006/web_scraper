# Generated by Django 3.0.4 on 2020-03-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraper_app', '0012_image_local_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='test',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AddField(
            model_name='webpage',
            name='test',
            field=models.CharField(default='', max_length=1),
        ),
    ]
