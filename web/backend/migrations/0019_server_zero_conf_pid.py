# Generated by Django 3.1.3 on 2020-11-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_server_hass_comp_installed'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='zero_conf_pid',
            field=models.IntegerField(null=True),
        ),
    ]
