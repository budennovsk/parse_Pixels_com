# Generated by Django 4.2 on 2023-04-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parse", "0006_alter_data_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="img_file",
            field=models.FileField(default=1, upload_to="specs"),
            preserve_default=False,
        ),
    ]
