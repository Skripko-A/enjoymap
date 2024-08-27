# Generated by Django 4.2 on 2024-08-27 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_image_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.location', verbose_name='Локация'),
        ),
    ]
