# Generated by Django 5.1.1 on 2024-10-16 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_staff_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='username',
        ),
    ]
