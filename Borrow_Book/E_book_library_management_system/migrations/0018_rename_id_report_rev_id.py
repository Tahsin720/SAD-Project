# Generated by Django 3.2.9 on 2021-12-24 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0017_auto_20211224_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='Id',
            new_name='Rev_Id',
        ),
    ]
