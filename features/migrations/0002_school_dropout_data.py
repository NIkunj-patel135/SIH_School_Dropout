# Generated by Django 4.2.5 on 2023-09-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='school_dropout_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_name', models.CharField(max_length=60)),
                ('school_name', models.CharField(max_length=60)),
                ('school_region', models.CharField(max_length=60)),
                ('school_district', models.CharField(max_length=60)),
            ],
        ),
    ]
