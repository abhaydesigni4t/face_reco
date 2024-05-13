# Generated by Django 5.0.1 on 2024-05-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_userenrolled_facial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='userenrolled',
            name='facial_data',
            field=models.ImageField(blank=True, null=True, upload_to='facial_data/', verbose_name='Facial Data'),
        ),
        migrations.DeleteModel(
            name='FacialDataImage',
        ),
    ]
