# Generated by Django 4.0.1 on 2022-01-14 09:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0016_alter_ad_expirationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='expirationTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 13, 9, 49, 43, 291817, tzinfo=utc), verbose_name='expiration time (of ad)'),
        ),
    ]
