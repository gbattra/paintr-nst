# Generated by Django 2.2.5 on 2020-02-20 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_service', '0003_auto_20200220_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestpainting',
            name='generated_image',
        ),
        migrations.RemoveField(
            model_name='requestpainting',
            name='painter_request',
        ),
        migrations.DeleteModel(
            name='PainterRequest',
        ),
        migrations.DeleteModel(
            name='RequestPainting',
        ),
    ]
