# Generated by Django 4.2.7 on 2023-11-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranslateHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('user_id', models.CharField(max_length=100)),
                ('user_app_version', models.CharField(max_length=100)),
                ('before_language_code', models.CharField(max_length=8)),
                ('before_content', models.TextField()),
                ('after_language_code', models.CharField(max_length=8)),
                ('after_content', models.TextField()),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
