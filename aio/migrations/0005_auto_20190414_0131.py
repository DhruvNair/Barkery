# Generated by Django 2.2 on 2019-04-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aio', '0004_auto_20190414_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shelter',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
