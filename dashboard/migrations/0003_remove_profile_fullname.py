# Generated by Django 5.0.4 on 2024-05-29 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_profile_city_alter_profile_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fullname',
        ),
    ]
