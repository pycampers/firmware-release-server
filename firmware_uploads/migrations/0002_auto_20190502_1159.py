# Generated by Django 2.2 on 2019-05-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmware_uploads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firmwareupload',
            options={'get_latest_by': ('major_version', 'minor_version', 'patch_version')},
        ),
        migrations.AddField(
            model_name='firmwareupload',
            name='deferred',
            field=models.BooleanField(default=False),
        ),
    ]
