# Generated by Django 3.2.6 on 2021-08-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0013_auto_20210814_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]
