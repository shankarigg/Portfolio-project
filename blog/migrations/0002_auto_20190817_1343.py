# Generated by Django 2.2.4 on 2019-08-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='msg_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
