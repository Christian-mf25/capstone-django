# Generated by Django 4.0.4 on 2022-05-31 13:40

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('description', models.TextField()),
                ('amount_collected', models.IntegerField(default=0)),
                ('finished', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(editable=False)),
                ('is_activated', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
