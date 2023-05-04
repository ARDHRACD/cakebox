# Generated by Django 4.1.4 on 2023-05-04 05:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='matter',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_deliverydate',
            field=models.DateTimeField(default=datetime.date(2023, 5, 5)),
        ),
    ]