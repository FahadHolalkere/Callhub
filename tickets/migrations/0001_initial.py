# Generated by Django 5.0.2 on 2024-02-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Technical', 'Technical'), ('Billing', 'Billing'), ('Service', 'Service')], max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('status', models.CharField(default='Open', max_length=20)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]