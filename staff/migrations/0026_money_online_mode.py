# Generated by Django 4.1 on 2024-05-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0025_alter_order_order_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='online_mode',
            field=models.BooleanField(default=False),
        ),
    ]
