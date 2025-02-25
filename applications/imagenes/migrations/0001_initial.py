# Generated by Django 5.1.4 on 2025-01-21 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reporte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('image', models.ImageField(upload_to='reunion', verbose_name='Imagen')),
                ('reunion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='reporte.reporte')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
