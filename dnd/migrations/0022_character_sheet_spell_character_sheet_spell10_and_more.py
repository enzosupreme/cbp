# Generated by Django 4.2.5 on 2024-03-30 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0021_alter_spell_damage'),
    ]

    operations = [
        migrations.AddField(
            model_name='character_sheet',
            name='spell',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell', to='dnd.spell'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='spell10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell10', to='dnd.spell'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='spell2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell2', to='dnd.spell'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='spell3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell3', to='dnd.spell'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='spell4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell4', to='dnd.spell'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='spell5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell5', to='dnd.spell'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='spell6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell6', to='dnd.spell'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='spell7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell7', to='dnd.spell'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='spell8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell8', to='dnd.spell'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='spell9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell9', to='dnd.spell'),
        ),
    ]