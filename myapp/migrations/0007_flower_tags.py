# Generated by Django 2.1.3 on 2022-02-20 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='tags',
            field=models.ManyToManyField(to='myapp.Tag'),
        ),
    ]
