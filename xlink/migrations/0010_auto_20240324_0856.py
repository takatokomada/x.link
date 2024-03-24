# Generated by Django 3.2.25 on 2024-03-23 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xlink', '0009_auto_20240324_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('高校生', '高校生'), ('中学生', '中学生'), ('小学生', '小学生'), ('社会人', '社会人'), ('大学生', '大学生')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('運動', '運動'), ('読書', '読書'), ('ゲーム', 'ゲーム'), ('VR/AR', 'VR/AR'), ('プログラミング', 'プログラミング'), ('PC', 'PC'), ('映画', '映画'), ('TV', 'TV')], max_length=8),
        ),
        migrations.AlterField(
            model_name='rooter',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
