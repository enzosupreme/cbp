# Generated by Django 4.2.5 on 2024-03-01 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0010_alter_race_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='darkvision',
            field=models.BooleanField(default=False),
        ),
    ]