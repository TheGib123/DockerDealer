# Generated by Django 3.0.1 on 2020-06-18 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicles', '0008_auto_20200618_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='pic',
        ),
        migrations.CreateModel(
            name='CarPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicles.Car')),
            ],
        ),
    ]
