# Generated by Django 3.2.9 on 2021-12-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0008_alter_my_request_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='my_request',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='my_request_log',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
