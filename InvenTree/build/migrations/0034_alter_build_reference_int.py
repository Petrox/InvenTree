# Generated by Django 3.2.5 on 2021-12-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0033_auto_20211128_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='reference_int',
            field=models.BigIntegerField(default=0),
        ),
    ]