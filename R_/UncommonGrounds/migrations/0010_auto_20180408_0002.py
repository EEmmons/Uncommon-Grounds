# Generated by Django 2.0.2 on 2018-04-08 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UncommonGrounds', '0009_auto_20180407_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='location_images/glamour-shots-to-look.jpg', upload_to='location_images/'),
        ),
    ]
