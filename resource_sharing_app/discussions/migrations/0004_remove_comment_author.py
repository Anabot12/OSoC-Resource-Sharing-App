# Generated by Django 4.2.3 on 2023-08-02 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0003_comment_author_discussion_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
