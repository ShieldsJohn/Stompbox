# Generated by Django 3.2.25 on 2024-04-20 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_manufacturer_pedal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['-listing_date']},
        ),
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]