# Generated by Django 4.2.2 on 2023-06-25 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_alter_producto_imagen_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
    ]
