# Generated by Django 5.1.1 on 2024-10-04 21:37

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_type', models.CharField(choices=[('product_issue', 'Product Issue'), ('billing_issue', 'Billing Issue'), ('staff_behavior', 'Staff Behavior')], max_length=50)),
                ('details', models.TextField(verbose_name='Message')),
                ('status', models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], max_length=50)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='Format: +263778123456', max_length=128, region=None)),
                ('loyalty_number', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
