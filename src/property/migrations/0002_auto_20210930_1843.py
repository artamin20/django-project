# Generated by Django 2.1.5 on 2021-09-30 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]