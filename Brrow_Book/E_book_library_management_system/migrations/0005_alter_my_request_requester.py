# Generated by Django 3.2.9 on 2021-11-26 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0004_my_request_requester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_request',
            name='requester',
            field=models.CharField(max_length=20),
        ),
    ]
