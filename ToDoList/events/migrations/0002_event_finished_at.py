# Generated by Django 4.2.7 on 2023-11-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='finished_at',
            field=models.DateTimeField(null=True),
        ),
    ]
