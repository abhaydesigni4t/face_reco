# Generated by Django 5.0.1 on 2024-05-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_orientation_attachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='userenrolled',
            name='my_comply',
            field=models.ImageField(blank=True, null=True, upload_to='compliance_images/'),
        ),
    ]