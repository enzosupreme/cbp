# Generated by Django 4.2.5 on 2024-04-01 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0031_monster'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='monsters1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster', to='dnd.monster'),
        ),
        migrations.AddField(
            model_name='map',
            name='monsters2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster2', to='dnd.monster'),
        ),
        migrations.AddField(
            model_name='map',
            name='monsters3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster3', to='dnd.monster'),
        ),
        migrations.AddField(
            model_name='map',
            name='monsters4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster4', to='dnd.monster'),
        ),
        migrations.AddField(
            model_name='map',
            name='monsters5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster5', to='dnd.monster'),
        ),
        migrations.AddField(
            model_name='map',
            name='monsters6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster6', to='dnd.monster'),
        ),
    ]
