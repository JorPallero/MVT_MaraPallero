# Generated by Django 4.1.1 on 2022-10-03 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miPrimerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='parentesco',
            field=models.CharField(max_length=10),
        ),
    ]
