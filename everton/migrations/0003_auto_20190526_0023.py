# Generated by Django 2.2.1 on 2019-05-25 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('everton', '0002_newspost_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspost',
            old_name='created_at',
            new_name='published_on',
        ),
    ]
