# Generated by Django 5.2 on 2025-05-07 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talep', '0009_alter_arac_kapasite_alter_arac_marka_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taleponay',
            name='sofor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='talep.sofor'),
        ),
    ]
