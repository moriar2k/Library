# Generated by Django 3.2.3 on 2021-06-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshelf',
            name='quantity',
            field=models.IntegerField(default=8),
        ),
    ]
