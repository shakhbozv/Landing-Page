# Generated by Django 4.0.2 on 2022-08-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('skill_thumb', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
