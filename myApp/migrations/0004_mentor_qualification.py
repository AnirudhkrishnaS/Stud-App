# Generated by Django 4.2.6 on 2024-01-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_session_from_date_remove_session_to_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='qualification',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
