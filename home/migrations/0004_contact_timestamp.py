# Generated by Django 3.0.6 on 2020-07-02 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200702_0641'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='timeStamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
