# Generated by Django 4.2.5 on 2024-03-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0022_character_sheet_spell_character_sheet_spell10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spell',
            name='damage',
            field=models.TextField(max_length=2055),
        ),
    ]
