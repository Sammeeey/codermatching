# Generated by Django 4.0.1 on 2022-02-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codermatch', '0045_ad_creatoremail'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='showEmailPublic',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
    ]
