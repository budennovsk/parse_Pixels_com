# Generated by Django 4.2 on 2023-04-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parse", "0005_alter_data_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="p"),
        ),
    ]
