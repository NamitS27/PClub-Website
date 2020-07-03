# Generated by Django 3.0.6 on 2020-07-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('logo', models.ImageField(default='default.png', upload_to='')),
                ('date', models.DateTimeField(default=None)),
                ('can_register', models.BooleanField(blank=True, default=False)),
                ('feedback_link', models.URLField(blank=True, default=None)),
                ('photos_link', models.URLField(blank=True)),
                ('registration_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('registration_link', models.URLField(blank=True)),
            ],
        ),
    ]
