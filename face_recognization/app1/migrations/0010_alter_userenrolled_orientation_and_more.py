# Generated by Django 5.0.1 on 2024-05-13 12:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_userenrolled_facial_data_delete_facialdataimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userenrolled',
            name='orientation',
            field=models.FileField(null=True, upload_to='attachments/', validators=[django.core.validators.FileExtensionValidator(['jpeg', 'jpg'])]),
        ),
        migrations.AlterField(
            model_name='userenrolled',
            name='tag_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
