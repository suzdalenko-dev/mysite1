# Generated by Django 5.1 on 2024-08-30 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='state',
        ),
    ]
