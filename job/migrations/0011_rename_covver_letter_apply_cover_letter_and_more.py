# Generated by Django 4.1.3 on 2022-12-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_apply_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='covver_letter',
            new_name='cover_letter',
        ),
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]