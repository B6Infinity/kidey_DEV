# Generated by Django 4.2.13 on 2024-05-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0031_rename_globalvariables_globalvariable'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverylandmark',
            name='parent',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
