# Generated by Django 4.2 on 2024-08-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0002_remove_costs_deadline_remove_costs_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='owner',
            field=models.IntegerField(),
        ),
    ]
