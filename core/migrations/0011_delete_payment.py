# Generated by Django 2.2.14 on 2022-06-16 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_address_default'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
