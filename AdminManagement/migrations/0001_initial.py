# Generated by Django 2.2 on 2020-09-20 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_name', models.CharField(max_length=100)),
                ('Admin_email', models.EmailField(max_length=100, unique=True)),
                ('Admin_contact', models.IntegerField(unique=True)),
            ],
        ),
    ]