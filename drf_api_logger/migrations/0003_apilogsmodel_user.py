# Generated by Django 3.0.8 on 2022-08-22 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drf_api_logger', '0002_auto_20211221_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='apilogsmodel',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
