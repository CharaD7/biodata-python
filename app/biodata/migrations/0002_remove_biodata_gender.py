# Generated by Django 2.2.9 on 2019-12-28 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biodata',
            name='gender',
        ),
    ]
