# Generated by Django 4.0 on 2022-01-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
