# Generated by Django 5.0.4 on 2024-04-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='rate',
            field=models.FloatField(),
        ),
    ]
