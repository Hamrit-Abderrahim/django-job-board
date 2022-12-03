# Generated by Django 4.1.3 on 2022-12-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('PART TIME', 'PART TIME'), ('FULL TIME', 'FULL TIME')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]