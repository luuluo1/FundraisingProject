# Generated by Django 2.1.5 on 2019-02-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksapp', '0002_auto_20190210_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='activation_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
