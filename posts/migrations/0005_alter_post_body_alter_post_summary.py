# Generated by Django 4.0.3 on 2022-03-21 09:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
