# Generated by Django 4.2.5 on 2024-03-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0020_spell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='damage',
            field=models.TextField(max_length=1055),
        ),
    ]
