# Generated by Django 2.2.4 on 2019-08-17 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190817_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]