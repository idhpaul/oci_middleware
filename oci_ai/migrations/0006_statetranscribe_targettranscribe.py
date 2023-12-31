# Generated by Django 4.2.7 on 2023-11-22 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oci_ai', '0005_alter_translatehistory_userappversion'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateTranscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiVersion', models.CharField(max_length=10)),
                ('user', models.JSONField()),
                ('timestamp', models.DateTimeField()),
                ('data', models.JSONField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TargetTranscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiVersion', models.CharField(max_length=10)),
                ('user', models.JSONField()),
                ('timestamp', models.DateTimeField()),
                ('data', models.JSONField()),
            ],
            options={
                'managed': False,
            },
        ),
    ]
