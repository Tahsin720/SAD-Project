# Generated by Django 3.2.9 on 2021-12-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0021_auto_20211224_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log_of_report',
            name='id',
        ),
        migrations.AlterField(
            model_name='log_of_report',
            name='date_time',
            field=models.DateTimeField(primary_key=True, serialize=False),
        ),
    ]
