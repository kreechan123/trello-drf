# Generated by Django 3.0.4 on 2020-03-10 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20200310_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='board',
            new_name='boardlist',
        ),
    ]
