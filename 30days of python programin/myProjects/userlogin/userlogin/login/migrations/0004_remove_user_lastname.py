# Generated by Django 4.2 on 2023-05-04 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
    ]