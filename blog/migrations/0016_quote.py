# Generated by Django 2.0.13 on 2019-06-16 06:04

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190616_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qauthor', models.CharField(max_length=200)),
                ('qdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('qtext', ckeditor.fields.RichTextField()),
            ],
        ),
    ]