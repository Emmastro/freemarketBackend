# Generated by Django 3.0.3 on 2020-03-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_auto_20200312_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useralamau',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useralamau',
            name='category',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='useralamau',
            name='notification_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
