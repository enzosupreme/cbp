# Generated by Django 4.2.5 on 2023-11-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gifter', models.CharField(blank=True, max_length=75, null=True)),
                ('giftee', models.CharField(blank=True, max_length=75, null=True)),
            ],
        ),
    ]