# Generated by Django 3.2.6 on 2021-08-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0014_alter_customer_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payable_amt',
            field=models.IntegerField(default=0),
        ),
    ]
