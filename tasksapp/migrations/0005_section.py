# Generated by Django 2.1.5 on 2019-01-31 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksapp', '0004_auto_20181125_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]