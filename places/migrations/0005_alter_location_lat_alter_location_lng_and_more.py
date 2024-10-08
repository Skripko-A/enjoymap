# Generated by Django 4.2 on 2024-08-27 08:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20240827_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=14, max_digits=18, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=14, max_digits=18, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='location',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='location',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
    ]
