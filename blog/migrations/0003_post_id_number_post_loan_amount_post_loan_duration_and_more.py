# Generated by Django 4.1.7 on 2023-03-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='id_number',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='loan_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='loan_duration',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='post',
            name='loan_interest',
            field=models.FloatField(default=0.02),
        ),
        migrations.AddField(
            model_name='post',
            name='loan_name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
