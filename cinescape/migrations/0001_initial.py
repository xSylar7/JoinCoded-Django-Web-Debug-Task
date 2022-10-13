# Generated by Django 4.1.2 on 2022-10-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('G', 'General'), ('PG', 'Parental Guidance'), ('R', 'Adult Guardian'), ('X', 'Restricted')], max_length=2)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geolocation', models.CharField(max_length=250)),
                ('area_name', models.CharField(max_length=50)),
                ('address_one', models.CharField(max_length=250)),
                ('address_two', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('released_at', models.DateField()),
                ('description', models.TextField()),
                ('poster', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
                ('booked_seats', models.PositiveIntegerField()),
            ],
        ),
    ]
