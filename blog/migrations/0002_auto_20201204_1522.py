# Generated by Django 3.1.3 on 2020-12-04 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_datetime',
            new_name='comment_datetime',
        ),
    ]