# Generated by Django 3.0.6 on 2020-07-02 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200702_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Phone',
            field=models.CharField(default='0911xxxxxx', max_length=13),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='abc@xxxxxx.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='Enter Your Name', max_length=255),
        ),
    ]
