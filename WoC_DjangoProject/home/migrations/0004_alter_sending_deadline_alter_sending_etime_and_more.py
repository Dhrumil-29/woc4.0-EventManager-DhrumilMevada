# Generated by Django 4.0 on 2022-01-19 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_event_registration_sending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='deadline',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sending',
            name='etime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sending',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sending',
            name='stime',
            field=models.DateTimeField(),
        ),
    ]