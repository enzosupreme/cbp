# Generated by Django 4.2.5 on 2024-05-23 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0039_special_item_rarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='special_item',
            name='lvl1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='special_item',
            name='lvl2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='special_item',
            name='lvl3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='special_item',
            name='lvl4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='special_item',
            name='lvl5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='special_item',
            name='lvl6',
            field=models.BooleanField(default=False),
        ),
    ]