# Generated by Django 5.1.1 on 2024-09-22 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_names_delete_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Names',
            new_name='Name',
        ),
    ]
