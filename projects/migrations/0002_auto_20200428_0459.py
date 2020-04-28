# Generated by Django 3.0.5 on 2020-04-28 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='projects',
            name='tages',
            field=models.ManyToManyField(blank=True, to='projects.Tags'),
        ),
    ]