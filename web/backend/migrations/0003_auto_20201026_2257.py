# Generated by Django 3.1.2 on 2020-10-26 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20201026_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='setup',
            field=models.CharField(default='step 0', max_length=10, null=True),
        ),
    ]
