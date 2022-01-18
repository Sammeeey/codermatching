# Generated by Django 4.0.1 on 2022-01-12 07:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0012_alter_ad_expirationdate_alter_ad_projectdescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='expirationDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 11, 7, 5, 40, 190629, tzinfo=utc), verbose_name='expiration date (of ad)'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codermatch.ad'),
        ),
    ]
