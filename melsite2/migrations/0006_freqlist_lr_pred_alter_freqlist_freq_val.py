# Generated by Django 4.2.4 on 2023-08-15 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("melsite2", "0005_city_freqlist_delete_candidate_city_cityname"),
    ]

    operations = [
        migrations.AddField(
            model_name="freqlist",
            name="lr_pred",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="freqlist",
            name="freq_val",
            field=models.FloatField(default=0.0),
        ),
    ]