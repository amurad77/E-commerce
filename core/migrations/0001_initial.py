# Generated by Django 3.2.4 on 2021-10-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=125, verbose_name='First Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('last_name', models.CharField(max_length=125, verbose_name='Last Name')),
                ('phone_number', models.CharField(blank=True, help_text='Contact phone number', max_length=15)),
                ('message', models.TextField(blank=True, max_length=1000, verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='Enter you email')),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
