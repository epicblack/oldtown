# Generated by Django 2.0.5 on 2018-08-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_auto_20180824_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='nombre',
            field=models.CharField(default='Cliente', max_length=20),
        ),
    ]
