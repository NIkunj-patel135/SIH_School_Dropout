# Generated by Django 4.2.5 on 2023-09-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_school_dropout_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_dropout_data',
            name='drop_out_number',
            field=models.IntegerField(default=0),
        ),
    ]
