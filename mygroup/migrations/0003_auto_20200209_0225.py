# Generated by Django 2.2.9 on 2020-02-09 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygroup', '0002_auto_20200209_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.IntegerField(default=0),
        ),
    ]
