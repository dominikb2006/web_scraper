# Generated by Django 3.0.4 on 2020-03-20 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraper_app', '0007_auto_20200320_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(default='', max_length=5000)),
                ('photo', models.ImageField(upload_to='images/')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_scraper_app.WebPage')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
