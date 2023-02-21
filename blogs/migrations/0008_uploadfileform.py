# Generated by Django 4.1.5 on 2023-02-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_delete_uploadfileform'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Register', models.DateTimeField()),
                ('Date_Act_Notice', models.DateTimeField()),
                ('Date_Act_Use', models.DateTimeField()),
                ('Act_Type', models.TextField()),
                ('Act_Name_TH', models.CharField(max_length=100, verbose_name='Enter Act Name')),
                ('Act_Name_ENG', models.CharField(max_length=100, verbose_name='Enter Act Name')),
                ('Act_Year', models.TextField()),
                ('Act_Status', models.TextField()),
                ('Act_Reason', models.TextField()),
                ('Act_Description', models.TextField()),
                ('Act_Freq_Repeat', models.IntegerField()),
                ('Act_Response_Department', models.TextField()),
                ('Act_Department_Effect', models.TextField()),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'act_pdf',
            },
        ),
    ]
