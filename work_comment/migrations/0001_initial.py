# Generated by Django 4.0 on 2022-01-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_title', models.CharField(max_length=15)),
                ('comment_company', models.CharField(max_length=15)),
                ('comment_score', models.IntegerField()),
                ('comment_context', models.CharField(max_length=256)),
            ],
        ),
    ]
