# Generated by Django 2.2.5 on 2020-02-20 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('painter_service', '0003_auto_20200220_1111'),
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