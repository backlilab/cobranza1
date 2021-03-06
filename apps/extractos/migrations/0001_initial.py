# Generated by Django 3.2.9 on 2021-12-01 11:11

import apps.extractos.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('bancos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extracto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_actualizacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('fecha', models.DateField()),
                ('archivo', models.FileField(upload_to=apps.extractos.models.content_file_name)),
                ('cuenta_bancaria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bancos.cuentabancaria')),
            ],
            options={
                'verbose_name': 'Extracto',
                'verbose_name_plural': 'Extractos',
                'db_table': 'cobranza_extracto',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_actualizacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('fecha', models.DateField()),
                ('referencia', models.CharField(max_length=250)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=12)),
                ('numero_operacion', models.CharField(max_length=50)),
                ('pertenece_cobranza', models.BooleanField(default=False)),
                ('itf', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('saldo', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('sucursal', models.CharField(blank=True, max_length=50, null=True)),
                ('referencia2', models.CharField(blank=True, max_length=250, null=True)),
                ('detalle', models.CharField(blank=True, max_length=250, null=True)),
                ('cargo', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('numero_doc', models.CharField(blank=True, max_length=250, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.cliente')),
                ('extracto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='extractos.extracto')),
            ],
            options={
                'verbose_name': 'Transaccion',
                'verbose_name_plural': 'Transacciones',
                'db_table': 'cobranza_transaccion',
                'ordering': ['-id'],
            },
        ),
    ]
