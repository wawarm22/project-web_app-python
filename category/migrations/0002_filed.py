# Generated by Django 4.0.2 on 2022-11-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filed', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]