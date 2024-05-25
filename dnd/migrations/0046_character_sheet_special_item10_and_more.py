# Generated by Django 4.2.5 on 2024-05-24 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnd', '0045_shop_item7'),
    ]

    operations = [
        migrations.AddField(
            model_name='character_sheet',
            name='special_item10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item0', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item11',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item11', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item12',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item12', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item13',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sspecial_item13', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item14',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item14', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item15',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item15', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item16',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item16', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item17',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item17', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item2', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item3', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item4', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item5', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item6', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item7', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item8', to='dnd.special_item'),
        ),
        migrations.AddField(
            model_name='character_sheet',
            name='special_item9',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='special_item9', to='dnd.special_item'),
        ),
    ]