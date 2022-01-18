# Generated by Django 4.0.1 on 2022-01-10 08:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0009_alter_ad_expirationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 8, 1, 53, 773335, tzinfo=utc), verbose_name='expiration date (of ad)'),
        ),
    ]
