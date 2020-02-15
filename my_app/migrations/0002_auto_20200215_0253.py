# Generated by Django 3.0.3 on 2020-02-15 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=150)),
                ('state', models.CharField(choices=[('Inactive', '0'), ('Active', '1')], default='Active', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Post')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='post',
            field=models.ManyToManyField(through='my_app.Details', to='my_app.Post'),
        ),
    ]
