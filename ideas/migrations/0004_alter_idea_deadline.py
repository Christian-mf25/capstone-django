# Generated by Django 4.0.4 on 2022-06-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_alter_idea_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='deadline',
            field=models.DateTimeField(editable=False),
        ),
    ]