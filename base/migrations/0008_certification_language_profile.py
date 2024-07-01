# Generated by Django 5.0.6 on 2024-06-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_title', models.CharField(blank=True, max_length=50, null=True)),
                ('cert_date', models.DateField(default=None)),
                ('cert_institute', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('language_proficiency', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_title', models.CharField(blank=True, max_length=50, null=True)),
                ('back_img', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('about_img', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('x_url', models.URLField(blank=True, null=True)),
                ('vimeo_url', models.URLField(blank=True, null=True)),
                ('discord_url', models.URLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
