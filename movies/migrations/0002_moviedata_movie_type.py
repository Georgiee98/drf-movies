# Generated by Django 3.2.18 on 2023-05-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='movie_type',
            field=models.CharField(default='action', max_length=255),
        ),
    ]
