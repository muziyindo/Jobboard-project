# Generated by Django 3.1 on 2021-07-11 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Job', '0002_auto_20210710_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='employer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
