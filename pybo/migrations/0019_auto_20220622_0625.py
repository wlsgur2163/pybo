# Generated by Django 3.1.3 on 2022-06-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0018_auto_20220622_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='QuestionCount',
        ),
    ]