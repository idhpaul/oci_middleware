# Generated by Django 4.2.7 on 2023-11-23 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oci_ai', '0007_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoCaption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languageCode', models.CharField(max_length=8)),
                ('caption', models.TextField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='captions', to='oci_ai.video')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
