# Generated by Django 2.2.6 on 2019-11-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtrack', '0031_auto_20191122_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
