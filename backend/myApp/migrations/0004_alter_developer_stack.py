# Generated by Django 4.0.2 on 2022-08-13 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_developer_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='stack',
            field=models.CharField(choices=[('Full-stack', 'Full-stack'), ('Frontend', 'Frontend'), ('Backend', 'Backend')], max_length=255),
        ),
    ]
