# Generated by Django 4.2.5 on 2024-03-01 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0006_enemy_str'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Stats',
                'ordering': ('name',),
            },
        ),
    ]
