# Generated by Django 4.2.5 on 2024-05-22 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0038_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='special_item',
            name='rarity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rare', to='dnd.rarity'),
        ),
    ]
