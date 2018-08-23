# Generated by Django 2.0.5 on 2018-08-23 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
        ('inventario', '0001_initial'),
        ('beneficios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venta', models.BooleanField(default=True)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bebida', models.BooleanField(default=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('total', models.PositiveIntegerField(null=True)),
                ('barbero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.Persona')),
                ('cliente', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='personas.Persona')),
                ('convenio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='beneficios.Convenio')),
                ('referido', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='personas.Persona')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='recibo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Recibo'),
        ),
        migrations.AddField(
            model_name='orden',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Servicio'),
        ),
    ]