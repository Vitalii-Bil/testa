# Generated by Django 3.1.6 on 2021-02-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210205_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='moderated',
            field=models.BooleanField(default=False, verbose_name='moderated'),
        ),
    ]
