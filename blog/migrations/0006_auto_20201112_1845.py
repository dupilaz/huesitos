# Generated by Django 3.1.2 on 2020-11-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_reclamo_apellidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Servicios'),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='Asunto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='Correo',
            field=models.EmailField(max_length=50),
        ),
    ]
