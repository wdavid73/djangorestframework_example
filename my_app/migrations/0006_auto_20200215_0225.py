# Generated by Django 3.0.3 on 2020-02-15 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_authorpost_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='post',
        ),
        migrations.AddField(
            model_name='author',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_app.Post'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AuthorPost',
        ),
    ]