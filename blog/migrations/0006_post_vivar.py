# Generated by Django 3.0.6 on 2020-07-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200704_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vivar',
            field=models.IntegerField(default=0),
        ),
    ]
