# Generated by Django 3.1 on 2021-07-17 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0005_auto_20210717_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='employer_email',
            field=models.EmailField(max_length=200),
        ),
    ]