# Generated by Django 3.1.6 on 2021-03-06 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_cartitem'),
        ('payment_module', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvoiceDetails',
            new_name='InvoiceDetail',
        ),
    ]
