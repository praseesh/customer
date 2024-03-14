# Generated by Django 5.0.3 on 2024-03-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=20, unique=True, verbose_name='Name')),
                ('lastname', models.CharField(blank=True, max_length=20, verbose_name='Surname')),
                ('address', models.CharField(max_length=20)),
                ('phno', models.BigIntegerField(blank=True, null=True, verbose_name='Phone Number')),
            ],
            options={
                'db_table': 'demoapp_Customer',
            },
        ),
    ]
