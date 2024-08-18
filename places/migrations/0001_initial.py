# Generated by Django 4.2 on 2024-08-12 18:25

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Название')),
                ('place_id', models.CharField(default='', max_length=100, unique=True)),
                ('description_short', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('description_long', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Подробное описание')),
                ('lng', models.DecimalField(decimal_places=14, default=37.61556, max_digits=18, verbose_name='Долгота')),
                ('lat', models.DecimalField(decimal_places=14, default=55.75222, max_digits=18, verbose_name='Широта')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(null=True, upload_to='places/images', verbose_name='Картинка')),
                ('position', models.PositiveIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='Позиция')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='places.location')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
