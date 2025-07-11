# Generated by Django 3.2 on 2025-07-03 07:17

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0002_auto_20250703_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('message', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('message', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='ServiceContent')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='AboutUs',
            new_name='AboutU',
        ),
        migrations.RenameModel(
            old_name='OurServices',
            new_name='OurService',
        ),
        migrations.RenameModel(
            old_name='OurValues',
            new_name='OurValue',
        ),
    ]
