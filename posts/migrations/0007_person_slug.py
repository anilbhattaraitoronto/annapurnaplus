# Generated by Django 3.2 on 2021-04-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default='slug-is-slug', max_length=100),
            preserve_default=False,
        ),
    ]
