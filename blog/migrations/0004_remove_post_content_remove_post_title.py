# Generated by Django 4.1.7 on 2023-03-23 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_id_number_post_loan_amount_post_loan_duration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
