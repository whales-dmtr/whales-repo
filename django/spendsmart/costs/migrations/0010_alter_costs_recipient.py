# Generated by Django 4.2 on 2024-09-06 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_wallets_owner'),
        ('costs', '0009_alter_costs_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costs',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient_costs', to='wallet.users'),
        ),
    ]
