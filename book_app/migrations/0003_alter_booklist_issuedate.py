# Generated by Django 4.0.2 on 2022-04-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_booklist_issuedate_booklist_studentname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklist',
            name='issuedate',
            field=models.DateField(default='', max_length=50),
        ),
    ]
