# Generated by Django 3.2.9 on 2021-12-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0006_my_request_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]