# Generated by Django 3.2 on 2021-04-21 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.CharField(max_length=255),
        ),
    ]