# Generated by Django 5.1 on 2024-09-10 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0015_vehicledata_invoice_veh_invoice_367b29_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='vehicledata',
            name='invoice_veh_company_c6af3d_idx',
        ),
    ]
