# Generated by Django 4.1.2 on 2022-10-29 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kola', '0003_details_remove_loan_customer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Details',
            new_name='Detail',
        ),
    ]
