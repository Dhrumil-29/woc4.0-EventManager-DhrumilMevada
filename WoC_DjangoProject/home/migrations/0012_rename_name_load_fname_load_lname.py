# Generated by Django 4.0 on 2022-01-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_sending_fname_sending_lname_alter_sending_desc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='load',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='load',
            name='lname',
            field=models.CharField(default='', max_length=122),
        ),
    ]
