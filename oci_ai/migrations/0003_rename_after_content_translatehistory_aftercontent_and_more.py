# Generated by Django 4.2.7 on 2023-11-20 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oci_ai', '0002_resulttranslate_targettranslate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translatehistory',
            old_name='after_content',
            new_name='afterContent',
        ),
        migrations.RenameField(
            model_name='translatehistory',
            old_name='after_language_code',
            new_name='afterLanguageCode',
        ),
        migrations.RenameField(
            model_name='translatehistory',
            old_name='before_content',
            new_name='beforeContent',
        ),
        migrations.RenameField(
            model_name='translatehistory',
            old_name='before_language_code',
            new_name='beforeLanguageCode',
        ),
        migrations.RenameField(
            model_name='translatehistory',
            old_name='user_app_version',
            new_name='userAppVersion',
        ),
        migrations.RenameField(
            model_name='translatehistory',
            old_name='user_id',
            new_name='userID',
        ),
    ]
