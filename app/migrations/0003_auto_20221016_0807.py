# Generated by Django 3.1 on 2022-10-16 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20221016_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='user_id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='payer',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]