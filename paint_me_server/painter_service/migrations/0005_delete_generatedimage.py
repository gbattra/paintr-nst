# Generated by Django 2.2.5 on 2020-02-20 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_service', '0006_auto_20200220_1124'),
        ('painter_service', '0004_auto_20200220_1114'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeneratedImage',
        ),
    ]
