# Generated by Django 3.2 on 2025-07-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0006_rename_ourvishon_ourvision'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='Stride, Inc.', max_length=200)),
                ('address_line1', models.CharField(default='1355 Market St, Suite 900', max_length=200)),
                ('city_state_zip', models.CharField(default='San Francisco, CA 94103', max_length=200)),
                ('phone', models.CharField(default='(123) 456-7890', max_length=50)),
                ('author', models.CharField(default='Holger Koenemann', max_length=100)),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='favicons/')),
            ],
        ),
    ]
