# Generated by Django 3.2.9 on 2021-12-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0016_auto_20211224_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='id',
        ),
        migrations.RemoveField(
            model_name='report',
            name='review_Id',
        ),
        migrations.AddField(
            model_name='report',
            name='Id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
