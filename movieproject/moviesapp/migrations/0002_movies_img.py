# Generated by Django 4.2.2 on 2023-06-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='dfvdfghjk', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
