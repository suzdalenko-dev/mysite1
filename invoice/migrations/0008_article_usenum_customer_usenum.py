# Generated by Django 5.0.3 on 2024-08-28 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_alter_customer_cif'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='usenum',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='usenum',
            field=models.BigIntegerField(null=True),
        ),
    ]
