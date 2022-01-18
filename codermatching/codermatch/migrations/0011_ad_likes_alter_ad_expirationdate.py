# Generated by Django 4.0.1 on 2022-01-10 08:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0010_alter_ad_expirationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ad',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 8, 15, 52, 470060, tzinfo=utc), verbose_name='expiration date (of ad)'),
        ),
    ]
