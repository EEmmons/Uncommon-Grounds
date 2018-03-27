# Generated by Django 2.0.2 on 2018-03-27 20:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UncommonGrounds', '0003_auto_20180327_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_since',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
