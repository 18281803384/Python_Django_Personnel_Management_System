# Generated by Django 4.2 on 2023-04-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_alter_department_update_time_alter_personnel_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='account',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='登录账号'),
        ),
        migrations.AddField(
            model_name='personnel',
            name='password',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='登录密码'),
        ),
    ]