# Generated by Django 2.2.9 on 2019-12-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biodata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('date_of_employment', models.DateField()),
                ('position', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('supervisors', models.CharField(max_length=100)),
            ],
        ),
    ]