# Generated by Django 5.0.1 on 2024-05-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Exit',
        ),
        migrations.AddField(
            model_name='asset',
            name='location',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='time_log',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
