# Generated by Django 5.1.4 on 2024-12-24 22:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_propmodel_test_img_alter_propmodel_img1_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propmodel',
            options={'verbose_name': 'Propiedad', 'verbose_name_plural': 'Propiedades'},
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='balcon',
            field=models.BooleanField(default=False, verbose_name='Balcón'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='clientSale',
            field=models.BooleanField(default=False, verbose_name='Cliente Venta'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='description',
            field=models.TextField(blank=True, help_text='La descripción de la casa.', max_length=2000, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='doubleBedRooms',
            field=models.IntegerField(blank=True, help_text='El número de habitaciones dobles de la casa.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Habitaciones dobles'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='elevator',
            field=models.BooleanField(default=False, verbose_name='Ascensor'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='forSale',
            field=models.BooleanField(default=False, verbose_name='Para Venta'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='fullBathrooms',
            field=models.IntegerField(blank=True, help_text='El número de baños completos de la casa.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Baños completos'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='garage',
            field=models.BooleanField(default=False, verbose_name='Garaje'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='garden',
            field=models.BooleanField(default=False, verbose_name='Jardín'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='id',
            field=models.CharField(help_text='El identificador de una casa, debe ser único, no pueden haber más de una casas con un mismo identificador.', max_length=100, primary_key=True, serialize=False, verbose_name='Identificator'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 1'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img10',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 10'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img11',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 11'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img12',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 12'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img13',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 13'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img14',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 14'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img15',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 15'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img16',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 16'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img17',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 17'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img18',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 18'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img19',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 19'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 2'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img20',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 20'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img21',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 21'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img22',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 22'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img23',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 23'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img24',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 24'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img25',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 25'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img26',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 26'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img27',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 27'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img28',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 28'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img29',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 29'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 3'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img30',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 30'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 4'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img5',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 5'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img6',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 6'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img7',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 7'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img8',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 8'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='img9',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen 9'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='location',
            field=models.CharField(blank=True, help_text='La ubicación o direcciónde la casa.', max_length=200, null=True, verbose_name='Ubicación'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='mapImg',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='Imagen de mapa'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='numberOfBathR',
            field=models.IntegerField(blank=True, help_text='El número de baños de la casa.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Baños'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='numberOfRooms',
            field=models.IntegerField(blank=True, help_text='El número de habitaciones de la casa.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Habitaciones'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='plazaGarage',
            field=models.BooleanField(default=False, verbose_name='Plaza Garaje'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='pool',
            field=models.BooleanField(default=False, verbose_name='Piscina'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='El precio de la casa.', max_digits=15, null=True, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='simpleBathrooms',
            field=models.IntegerField(blank=True, help_text='El número de baños simples de la casa.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Baños simples'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='simpleBedRooms',
            field=models.IntegerField(blank=True, help_text='El número de habitaciones simples de la casa.', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Habitaciones simples'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='surface',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='La superficie o área de la casa.', max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)], verbose_name='Superficie'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='terraza',
            field=models.BooleanField(default=False, verbose_name='Terraza'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='title',
            field=models.CharField(blank=True, help_text='El titulo o nombre de la casa.', max_length=100, null=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='trastero',
            field=models.BooleanField(default=False, verbose_name='Trastero'),
        ),
        migrations.AlterField(
            model_name='propmodel',
            name='type',
            field=models.CharField(blank=True, help_text='El tipo de casa (piso, departamento, chalet, vivienda, etc.)', max_length=50, null=True, verbose_name='Tipo'),
        ),
    ]