# Generated by Django 2.0.2 on 2018-04-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UncommonGrounds', '0017_auto_20180422_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='faves', to='UncommonGrounds.Location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_tags',
            field=models.ManyToManyField(blank=True, to='UncommonGrounds.Tag'),
        ),
    ]