# Generated by Django 5.0.6 on 2024-05-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peopletype',
            name='img',
            field=models.ImageField(blank=True, upload_to='user_img'),
        ),
    ]
