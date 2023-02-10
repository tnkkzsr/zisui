# Generated by Django 4.1.5 on 2023-02-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_zisuipost_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zisuipost',
            name='author',
        ),
        migrations.AlterField(
            model_name='zisuipost',
            name='howtocook',
            field=models.TextField(default='作り方を入力', verbose_name='作り方'),
        ),
        migrations.AlterField(
            model_name='zisuipost',
            name='ingredients',
            field=models.TextField(default='材料を入力', max_length=128, verbose_name='材料'),
        ),
    ]