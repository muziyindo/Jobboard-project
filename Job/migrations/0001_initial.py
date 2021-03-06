# Generated by Django 3.1 on 2021-07-10 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_email', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('application_email_website', models.CharField(max_length=255)),
                ('closing_Date', models.DateField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=200)),
                ('company_website', models.CharField(max_length=200)),
                ('employer_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
