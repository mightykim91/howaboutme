# Generated by Django 3.1.2 on 2020-11-11 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.area'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.body'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.job'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.religion'),
        ),
    ]