# Generated by Django 3.2.9 on 2021-12-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0031_remove_review_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_time',
            field=models.DateTimeField(default='Not Set'),
        ),
    ]
