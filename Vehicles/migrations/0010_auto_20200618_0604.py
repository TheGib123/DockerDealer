# Generated by Django 3.0.1 on 2020-06-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0009_auto_20200618_0558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carpic',
            old_name='user',
            new_name='Car',
        ),
        migrations.AddField(
            model_name='carpic',
            name='pic',
            field=models.ImageField(default='gallery/error.png', upload_to='gallery'),
        ),
    ]