# Generated by Django 3.2.25 on 2024-05-10 06:52

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20240508_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, max_digits=6),
        ),
    ]
