# Generated by Django 5.0.3 on 2024-08-28 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_remove_article_invoice_art_name_712290_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cif',
            field=models.CharField(max_length=33, null=True),
        ),
    ]
