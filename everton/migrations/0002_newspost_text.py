# Generated by Django 2.2.1 on 2019-05-25 00:00

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('everton', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='text',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]