# Generated by Django 4.2.11 on 2024-04-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screening_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='screeningguideline',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='screeningrule',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]