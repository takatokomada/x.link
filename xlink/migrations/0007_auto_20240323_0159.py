# Generated by Django 3.2.25 on 2024-03-22 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xlink', '0006_auto_20240321_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='detail',
            field=models.CharField(choices=[('高校生', '高校生'), ('大学生', '大学生'), ('中学生', '中学生'), ('社会人', '社会人'), ('小学生', '小学生')], max_length=8),
        ),
        migrations.AlterField(
            model_name='account',
            name='hobby',
            field=models.CharField(choices=[('PC', 'PC'), ('プログラミング', 'プログラミング'), ('読書', '読書'), ('ゲーム', 'ゲーム'), ('運動', '運動'), ('VR/AR', 'VR/AR'), ('映画', '映画'), ('TV', 'TV')], max_length=8),
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xlink.group')),
                ('recommending_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]