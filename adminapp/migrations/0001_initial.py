# Generated by Django 3.1.4 on 2021-08-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=50)),
                ('Mobile', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Administrator',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Library',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LibName', models.CharField(max_length=50)),
                ('Reviews', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Reviews',
            },
        ),
    ]