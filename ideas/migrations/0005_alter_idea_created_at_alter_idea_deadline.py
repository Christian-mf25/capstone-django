# Generated by Django 4.0.4 on 2022-06-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_alter_idea_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='deadline',
            field=models.DateField(editable=False),
        ),
    ]