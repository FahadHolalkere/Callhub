# Generated by Django 5.0.2 on 2024-02-14 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='last_modified_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
