# Generated by Django 3.1.2 on 2020-11-13 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_age', models.IntegerField(default=20)),
                ('max_age', models.IntegerField(default=50)),
                ('min_height', models.IntegerField(default=140)),
                ('max_height', models.IntegerField(default=200)),
                ('drink', models.CharField(max_length=10)),
                ('smoke', models.CharField(max_length=10)),
                ('area', models.ManyToManyField(related_name='preference', to='profiles.Area')),
                ('body', models.ManyToManyField(related_name='preference', to='profiles.Body')),
                ('education', models.ManyToManyField(related_name='preference', to='profiles.Education')),
                ('job', models.ManyToManyField(related_name='preference', to='profiles.Job')),
                ('religion', models.ManyToManyField(related_name='preference', to='profiles.Religion')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preference', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
