# Generated by Django 5.0.1 on 2024-05-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_onsiteuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onsiteuser',
            name='status',
            field=models.CharField(choices=[('Entry', 'Entry'), ('Exit', 'Exit')], max_length=100),
        ),
    ]