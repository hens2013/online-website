# Generated by Django 2.2.14 on 2022-06-15 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220615_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='slug2',
            new_name='slug',
        ),
    ]