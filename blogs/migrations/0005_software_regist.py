# Generated by Django 4.1.5 on 2023-02-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_delete_software_regist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software_Regist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Details', models.TextField()),
                ('License_Type', models.TextField()),
                ('License_User', models.TextField()),
                ('License_Number', models.TextField()),
                ('First_use_datetime', models.DateTimeField()),
                ('Start_use_datetime', models.DateTimeField()),
                ('End_use_datetime', models.DateTimeField()),
            ],
        ),
    ]
