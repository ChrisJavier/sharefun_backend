# Generated by Django 2.2.9 on 2020-02-09 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygroup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
