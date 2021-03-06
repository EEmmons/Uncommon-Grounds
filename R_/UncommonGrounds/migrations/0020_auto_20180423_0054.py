# Generated by Django 2.0.2 on 2018-04-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UncommonGrounds', '0019_auto_20180422_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='faves', to='UncommonGrounds.Location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_tags',
            field=models.ManyToManyField(to='UncommonGrounds.Tag'),
        ),
    ]
