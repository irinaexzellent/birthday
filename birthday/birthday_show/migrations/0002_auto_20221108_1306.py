# Generated by Django 2.2.16 on 2022-11-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True, verbose_name='date of birthday'),
        ),
    ]
