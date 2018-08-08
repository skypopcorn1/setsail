# Generated by Django 2.0.7 on 2018-08-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180807_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Club Administrator'), (2, 'Club Manager'), (3, 'Crew Captain'), (4, 'Crew Member'), (5, 'Deck Hand')], primary_key=True, serialize=False),
        ),
    ]