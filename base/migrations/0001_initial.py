# Generated by Django 5.0.6 on 2024-05-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_position', models.CharField(max_length=50)),
                ('work_date', models.DurationField()),
                ('work_company', models.CharField(max_length=50)),
                ('work_description', models.TextField()),
            ],
        ),
    ]
