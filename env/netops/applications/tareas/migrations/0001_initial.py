# Generated by Django 5.0.3 on 2024-07-05 19:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('tipo', models.CharField(choices=[('0', 'Tarea Operativa'), ('1', 'Tarea Programada'), ('2', 'Falla/Disturbio')], max_length=1, verbose_name='Tipo de tarea')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarea_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
            },
        ),
    ]
