# Generated by Django 3.0.1 on 2020-06-18 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0007_auto_20200618_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='pic',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]