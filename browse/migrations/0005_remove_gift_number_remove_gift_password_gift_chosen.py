# Generated by Django 4.2.5 on 2023-11-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0004_rename_gifter_gift_name_remove_gift_giftee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='number',
        ),
        migrations.RemoveField(
            model_name='gift',
            name='password',
        ),
        migrations.AddField(
            model_name='gift',
            name='chosen',
            field=models.BooleanField(default=False),
        ),
    ]
