# Generated by Django 4.2.16 on 2024-09-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
