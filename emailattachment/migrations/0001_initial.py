# Generated by Django 2.2.2 on 2023-01-01 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
    ]
