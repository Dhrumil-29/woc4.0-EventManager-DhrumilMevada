# Generated by Django 4.0 on 2022-01-20 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_sending_deadline_alter_sending_etime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('num', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=122)),
                ('nopar', models.CharField(max_length=10)),
                ('nevent', models.CharField(max_length=50)),
            ],
        ),
    ]