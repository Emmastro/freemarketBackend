# Generated by Django 3.0.3 on 2020-04-14 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descrption',
            new_name='description',
        ),
    ]
