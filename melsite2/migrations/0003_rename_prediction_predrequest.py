# Generated by Django 4.2.4 on 2023-08-15 08:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("melsite2", "0002_prediction"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Prediction",
            new_name="PredRequest",
        ),
    ]