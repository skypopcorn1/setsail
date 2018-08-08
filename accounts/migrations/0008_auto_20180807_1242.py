# Generated by Django 2.0.7 on 2018-08-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180807_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.IntegerField(choices=[(1, 'Club Administrator'), (2, 'Club Manager'), (3, 'Crew Manager'), (4, 'Crew Member'), (5, 'Deck Hand')], primary_key=True, serialize=False),
        ),
    ]
