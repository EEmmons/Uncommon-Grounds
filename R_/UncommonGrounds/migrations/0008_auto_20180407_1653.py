# Generated by Django 2.0.2 on 2018-04-07 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UncommonGrounds', '0007_location_contributor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='user',
            name='locations',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_tags',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='location',
            name='contributor',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
