# Generated by Django 4.2.11 on 2024-04-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]
