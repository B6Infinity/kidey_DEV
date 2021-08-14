# Generated by Django 3.2.6 on 2021-08-14 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0012_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=120),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_json', models.JSONField(null=True)),
                ('time_of_order', models.DateTimeField()),
                ('time_of_delivery', models.DateTimeField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('total_bill', models.IntegerField(default=0)),
                ('bill_text', models.TextField(blank=True, default='')),
                ('discount', models.IntegerField(default=0)),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.customer')),
            ],
        ),
    ]