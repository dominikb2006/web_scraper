# Generated by Django 3.0.4 on 2020-03-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraper_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='texts',
            name='text',
        ),
        migrations.AddField(
            model_name='webpage',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
