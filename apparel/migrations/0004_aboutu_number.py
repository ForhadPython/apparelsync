# Generated by Django 3.2 on 2025-07-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0003_auto_20250703_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutu',
            name='number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
