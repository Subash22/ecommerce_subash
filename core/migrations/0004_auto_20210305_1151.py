# Generated by Django 3.1.6 on 2021-03-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210305_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='registered_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]