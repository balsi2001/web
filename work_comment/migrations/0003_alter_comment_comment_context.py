# Generated by Django 4.0.1 on 2022-01-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_comment', '0002_comment_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_context',
            field=models.CharField(max_length=1000),
        ),
    ]
