# Generated by Django 3.2.4 on 2021-06-29 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_productos_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='banner',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
