# Generated by Django 4.2.11 on 2024-03-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='no_of_brk_points',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
