# Generated by Django 4.2 on 2024-09-03 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_alter_users_email'),
        ('costs', '0007_alter_costs_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.users'),
        ),
    ]
