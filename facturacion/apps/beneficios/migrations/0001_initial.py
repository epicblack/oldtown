# Generated by Django 2.0.5 on 2018-08-14 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_entidad', models.CharField(max_length=30)),
                ('porcentaje', models.IntegerField(default=0)),
                ('cerveza', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fidelizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_servicios', models.IntegerField(default=0)),
                ('cantidad_referidos', models.IntegerField(default=0)),
                ('cantidad_redenciones', models.IntegerField(default=0)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Referido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='personas.Persona')),
                ('refiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona')),
            ],
        ),
    ]
