# Generated by Django 4.2 on 2023-04-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_alter_department_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='create_time',
            field=models.CharField(max_length=19, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='department',
            name='update_time',
            field=models.CharField(default='', max_length=19, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='create_time',
            field=models.CharField(max_length=19, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='update_time',
            field=models.CharField(max_length=19, verbose_name='修改时间'),
        ),
    ]