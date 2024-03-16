# Generated by Django 3.2.25 on 2024-03-16 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('中学生', '中学生'), ('大学生', '大学生'), ('高校生', '高校生'), ('小学生', '小学生'), ('社会人', '社会人')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('PC', 'PC'), ('プログラミング', 'プログラミング'), ('運動', '運動'), ('ゲーム', 'ゲーム'), ('読書', '読書'), ('TV', 'TV'), ('VR/AR', 'VR/AR'), ('映画', '映画')], max_length=8),
        ),
    ]