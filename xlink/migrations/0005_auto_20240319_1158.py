# Generated by Django 3.2.25 on 2024-03-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlink', '0004_auto_20240319_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roots',
            old_name='rotter',
            new_name='rooter',
        ),
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('大学生', '大学生'), ('社会人', '社会人'), ('小学生', '小学生'), ('高校生', '高校生'), ('中学生', '中学生')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('プログラミング', 'プログラミング'), ('TV', 'TV'), ('ゲーム', 'ゲーム'), ('運動', '運動'), ('読書', '読書'), ('VR/AR', 'VR/AR'), ('映画', '映画'), ('PC', 'PC')], max_length=8),
        ),
    ]