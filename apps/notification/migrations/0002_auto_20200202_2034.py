# Generated by Django 3.0.2 on 2020-02-02 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='date',
            new_name='created',
        ),
    ]
