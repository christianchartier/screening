# Generated by Django 4.2.11 on 2024-04-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screening_app', '0002_screeningguideline_notes_screeningrule_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screeningrule',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
    ]
