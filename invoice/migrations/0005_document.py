# Generated by Django 5.1 on 2024-08-31 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_remove_article_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=41, null=True, unique=True)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='invoice_doc_id_f3c779_idx')],
            },
        ),
    ]
