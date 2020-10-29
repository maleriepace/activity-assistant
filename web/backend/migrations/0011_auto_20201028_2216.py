# Generated by Django 3.1.2 on 2020-10-28 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20201028_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='end',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='dataset',
            old_name='path_to_file',
            new_name='path_to_folder',
        ),
        migrations.RenameField(
            model_name='dataset',
            old_name='start',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='dataset',
            name='logging',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
