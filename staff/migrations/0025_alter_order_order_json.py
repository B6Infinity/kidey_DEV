# Generated by Django 4.1 on 2024-05-07 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0024_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_json',
            field=models.TextField(default={}),
            preserve_default=False,
        ),
    ]