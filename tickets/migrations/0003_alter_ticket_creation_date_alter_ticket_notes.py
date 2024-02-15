# Generated by Django 5.0.2 on 2024-02-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='notes',
            field=models.JSONField(default=list),
        ),
    ]