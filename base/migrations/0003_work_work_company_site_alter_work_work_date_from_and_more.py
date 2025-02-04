# Generated by Django 5.0.6 on 2024-05-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_work_work_date_work_work_date_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work_company_site',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_date_from',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_date_to',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
    ]
