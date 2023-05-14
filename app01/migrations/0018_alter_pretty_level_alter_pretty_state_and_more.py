# Generated by Django 4.2.1 on 2023-05-13 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0017_order_create_time_order_update_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pretty',
            name='level',
            field=models.SmallIntegerField(choices=[(4, '4级'), (2, '2级'), (1, '1级'), (3, '3级')], default=1, verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='pretty',
            name='state',
            field=models.SmallIntegerField(choices=[(1, '未使用'), (2, '已使用')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='taskmanager',
            name='level',
            field=models.SmallIntegerField(choices=[(3, '临时'), (2, '一般'), (1, '重要')], default=3, verbose_name='级别'),
        ),
    ]
