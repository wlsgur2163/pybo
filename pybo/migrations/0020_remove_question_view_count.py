# Generated by Django 3.1.3 on 2022-06-21 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0019_auto_20220622_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='view_count',
        ),
    ]