# Generated by Django 3.2.9 on 2021-11-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0003_rename_request_my_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_request',
            name='requester',
            field=models.CharField(default='NULL', max_length=20),
        ),
    ]
