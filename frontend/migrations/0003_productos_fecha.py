# Generated by Django 3.2.4 on 2021-06-28 03:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_productos_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]