# Generated by Django 3.0.6 on 2020-07-02 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=13)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
