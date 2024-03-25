# Generated by Django 3.2.25 on 2024-03-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlink', '0015_auto_20240324_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('高校生', '高校生'), ('中学生', '中学生'), ('社会人', '社会人'), ('小学生', '小学生'), ('大学生', '大学生')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('TV', 'TV'), ('読書', '読書'), ('映画', '映画'), ('運動', '運動'), ('PC', 'PC'), ('ゲーム', 'ゲーム'), ('VR/AR', 'VR/AR'), ('プログラミング', 'プログラミング')], max_length=8),
        ),
        migrations.AlterField(
            model_name='root',
            name='rooter',
            field=models.CharField(default=1, max_length=1000000),
            preserve_default=False,
        ),
    ]
