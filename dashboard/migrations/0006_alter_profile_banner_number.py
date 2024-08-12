# Generated by Django 5.0.4 on 2024-06-21 11:37

import dashboard.helper
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_profile_banner_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='banner_number',
            field=models.IntegerField(default=1, validators=[dashboard.helper.validate_range_banner]),
        ),
    ]
