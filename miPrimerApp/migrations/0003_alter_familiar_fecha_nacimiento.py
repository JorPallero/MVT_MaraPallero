# Generated by Django 4.1.1 on 2022-10-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miPrimerApp', '0002_alter_familiar_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
