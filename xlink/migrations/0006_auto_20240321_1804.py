# Generated by Django 3.2.25 on 2024-03-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlink', '0005_auto_20240319_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='root',
            name='rooter_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('社会人', '社会人'), ('中学生', '中学生'), ('小学生', '小学生'), ('高校生', '高校生'), ('大学生', '大学生')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('TV', 'TV'), ('映画', '映画'), ('読書', '読書'), ('プログラミング', 'プログラミング'), ('ゲーム', 'ゲーム'), ('PC', 'PC'), ('VR/AR', 'VR/AR'), ('運動', '運動')], max_length=8),
        ),
        migrations.DeleteModel(
            name='Roots',
        ),
    ]
