# Generated by Django 3.2 on 2021-04-21 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_blog_summary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('document', models.FileField(upload_to='events/uploads/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='posts.event')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.person')),
            ],
        ),
    ]
