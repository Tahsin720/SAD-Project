# Generated by Django 3.2.9 on 2021-12-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_book_library_management_system', '0033_auto_20211224_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review_for_books',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('posted_by', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('text', models.TextField(max_length=200)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
