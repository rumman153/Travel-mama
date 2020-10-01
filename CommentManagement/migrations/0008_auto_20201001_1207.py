# Generated by Django 2.2 on 2020-10-01 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileManagement', '0001_initial'),
        ('CommentManagement', '0007_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='User',
        ),
        migrations.AddField(
            model_name='comment',
            name='Profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProfileManagement.Profile'),
        ),
    ]