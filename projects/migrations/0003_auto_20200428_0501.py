# Generated by Django 3.0.5 on 2020-04-28 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200428_0459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={},
        ),
        migrations.RemoveField(
            model_name='projects',
            name='tages',
        ),
    ]