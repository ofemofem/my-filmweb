# Generated by Django 2.1.7 on 2019-03-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmweb', '0002_auto_20190317_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(),
        ),
    ]