# Generated by Django 4.2 on 2023-05-03 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0003_alter_collection_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='info',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
