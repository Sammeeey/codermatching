# Generated by Django 4.0.1 on 2022-02-10 06:37

import codermatch.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0037_alter_ad_expirationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='expirationTime',
            field=models.DateTimeField(default=codermatch.models.Ad.in30Days, verbose_name='expiration time (of ad)'),
        ),
    ]
