# Generated by Django 3.1.2 on 2020-10-28 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20201028_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='path_to_folder',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
