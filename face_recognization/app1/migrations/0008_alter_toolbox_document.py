# Generated by Django 5.0.1 on 2024-05-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_toolbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toolbox',
            name='document',
            field=models.FileField(upload_to='toolbox/'),
        ),
    ]
