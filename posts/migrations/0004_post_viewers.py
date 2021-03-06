# Generated by Django 4.0.3 on 2022-03-21 07:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_remove_post_views_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='viewers',
            field=models.ManyToManyField(related_name='post_viewers', to=settings.AUTH_USER_MODEL),
        ),
    ]
