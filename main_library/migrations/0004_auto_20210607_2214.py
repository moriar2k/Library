# Generated by Django 3.2.3 on 2021-06-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_library', '0003_rental_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental_list',
            name='date_of_return',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='rental_list',
            name='planned_date_of_return',
            field=models.DateTimeField(default=None),
        ),
    ]
