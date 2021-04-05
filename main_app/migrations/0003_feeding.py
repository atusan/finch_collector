# Generated by Django 3.1.6 on 2021-04-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210331_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal', models.CharField(choices=[('C', 'Cleaning'), ('D', 'Dusting'), ('F', 'Fixing')], default='C', max_length=1)),
            ],
        ),
    ]