# Generated by Django 3.2.9 on 2021-11-27 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=1, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
