# Generated by Django 3.1.5 on 2021-01-05 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='pw',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='board',
            name='username',
            field=models.CharField(max_length=10),
        ),
    ]
