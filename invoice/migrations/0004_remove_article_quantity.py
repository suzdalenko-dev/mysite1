# Generated by Django 5.1 on 2024-08-30 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0003_remove_article_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='quantity',
        ),
    ]
