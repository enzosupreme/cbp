# Generated by Django 4.2.5 on 2024-05-24 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0046_character_sheet_special_item10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character_sheet',
            name='special_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item', to='dnd.special_item'),
        ),
    ]
