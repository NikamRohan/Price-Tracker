# Generated by Django 3.1.7 on 2021-04-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20200910_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='url',
            field=models.CharField(max_length=2000),
        ),
    ]
