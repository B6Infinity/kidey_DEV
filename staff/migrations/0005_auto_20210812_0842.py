# Generated by Django 3.2.6 on 2021-08-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='total_bill',
            field=models.IntegerField(default=0),
        ),
    ]
