# Generated by Django 3.1.3 on 2023-05-21 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230521_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
            preserve_default=False,
        ),
    ]
