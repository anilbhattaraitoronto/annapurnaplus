# Generated by Django 3.2 on 2021-04-22 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_presentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.event'),
        ),
    ]
