# Generated by Django 4.2.5 on 2024-03-01 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0008_race_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='bonus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='race', to='dnd.stat'),
        ),
    ]