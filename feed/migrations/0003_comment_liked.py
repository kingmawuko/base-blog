# Generated by Django 4.0.1 on 2022-06-14 22:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0002_remove_postmodel_slug_postmodel_liked_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
