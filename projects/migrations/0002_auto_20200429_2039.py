# Generated by Django 3.0.5 on 2020-04-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
