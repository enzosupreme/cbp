# Generated by Django 4.2.5 on 2024-03-25 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0015_weapon_remove_character_sheet_abilities_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapon',
            name='bonus',
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='weapon2_bonus',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='weapon3_bonus',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='weapon_bonus',
            field=models.IntegerField(null=True),
        ),
    ]
