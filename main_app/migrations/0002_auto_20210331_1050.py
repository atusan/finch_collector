# Generated by Django 3.1.6 on 2021-03-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='art',
            name='age',
        ),
        migrations.RemoveField(
            model_name='art',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='art',
            name='description',
        ),
        migrations.AlterField(
            model_name='art',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]