# Generated by Django 3.2 on 2022-12-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dz_pro', '0004_auto_20221228_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
