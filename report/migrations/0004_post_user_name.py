# Generated by Django 4.1.1 on 2022-09-14 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0003_remove_post_update_post_modified_alter_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
