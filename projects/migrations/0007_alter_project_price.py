# Generated by Django 4.2.5 on 2023-10-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]