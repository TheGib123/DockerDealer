# Generated by Django 3.0.1 on 2020-06-18 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0003_auto_20200618_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='pic',
            field=models.ImageField(blank=True, default='gallery/error.png', null=True, upload_to='gallery'),
        ),
    ]