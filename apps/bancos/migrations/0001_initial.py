# Generated by Django 3.2.9 on 2021-11-30 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_actualizacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Bancos',
                'db_table': 'cobranza_banco',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CuentaBancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('usuario_creacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_actualizacion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, null=True)),
                ('numero', models.CharField(max_length=50, unique=True)),
                ('tipo_moneda', models.CharField(choices=[('PEN', 'Soles'), ('USD', 'Dolares')], default='PEN', max_length=3)),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bancos.banco')),
            ],
            options={
                'verbose_name': 'Numeros de cuenta',
                'db_table': 'cobranza_cuenta_bancaria',
                'ordering': ['-id'],
            },
        ),
    ]