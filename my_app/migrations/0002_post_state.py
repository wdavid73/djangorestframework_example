# Generated by Django 3.0.3 on 2020-02-15 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.SmallIntegerField(default=1),
        ),
    ]