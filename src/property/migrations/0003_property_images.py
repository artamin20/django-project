# Generated by Django 2.1.5 on 2021-10-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20210930_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='images',
            field=models.ImageField(null=True, upload_to='property/'),
        ),
    ]
