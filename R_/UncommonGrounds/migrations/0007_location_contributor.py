# Generated by Django 2.0.2 on 2018-03-30 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UncommonGrounds', '0006_auto_20180327_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='contributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UncommonGrounds.User'),
        ),
    ]
