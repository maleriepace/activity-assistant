# Generated by Django 3.1.2 on 2020-10-26 19:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='algorithm',
            name='compatible_dataset',
        ),
        migrations.RemoveField(
            model_name='algorithm',
            name='selected_dataset',
        ),
        migrations.RemoveField(
            model_name='algorithm',
            name='selected_person',
        ),
        migrations.RemoveField(
            model_name='benchmark',
            name='model',
        ),
        migrations.RemoveField(
            model_name='datainstance',
            name='dataset',
        ),
        migrations.DeleteModel(
            name='ModelComparision',
        ),
        migrations.AlterModelOptions(
            name='dataset',
            options={},
        ),
        migrations.RenameField(
            model_name='dataset',
            old_name='path_to_folder',
            new_name='path_to_file',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='name',
        ),
        migrations.RemoveField(
            model_name='device',
            name='component',
        ),
        migrations.RemoveField(
            model_name='model',
            name='algorithm',
        ),
        migrations.RemoveField(
            model_name='model',
            name='datainstance',
        ),
        migrations.RemoveField(
            model_name='server',
            name='hass_address',
        ),
        migrations.RemoveField(
            model_name='server',
            name='selected_algorithm',
        ),
        migrations.RemoveField(
            model_name='server',
            name='selected_dataset',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='logged_location',
        ),
        migrations.AddField(
            model_name='dataset',
            name='end',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataset',
            name='start',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='setup',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Algorithm',
        ),
        migrations.DeleteModel(
            name='Benchmark',
        ),
        migrations.DeleteModel(
            name='DataInstance',
        ),
        migrations.DeleteModel(
            name='DeviceComponent',
        ),
    ]
