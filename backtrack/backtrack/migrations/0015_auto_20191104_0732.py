# Generated by Django 2.2.6 on 2019-11-04 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backtrack', '0014_auto_20191104_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectparticipant',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectParticipant', to='backtrack.Project'),
        ),
    ]
