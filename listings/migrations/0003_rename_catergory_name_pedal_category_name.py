# Generated by Django 3.2.25 on 2024-05-30 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20240528_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedal',
            old_name='catergory_name',
            new_name='category_name',
        ),
    ]