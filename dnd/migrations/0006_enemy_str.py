# Generated by Django 4.2.5 on 2024-02-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0005_enemy'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='str',
            field=models.IntegerField(null=True),
        ),
    ]