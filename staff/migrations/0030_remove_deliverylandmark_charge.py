# Generated by Django 4.2.13 on 2024-05-14 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0029_globalvariables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverylandmark',
            name='charge',
        ),
    ]
