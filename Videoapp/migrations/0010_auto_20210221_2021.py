# Generated by Django 3.1.2 on 2021-02-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Videoapp', '0009_remove_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]
