# Generated by Django 4.1.6 on 2023-02-17 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('need_int', models.IntegerField()),
                ('need_social', models.IntegerField()),
                ('need_exp', models.IntegerField()),
                ('need_total_exp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('int_stat', models.IntegerField(default=0)),
                ('social_stat', models.IntegerField(default=0)),
                ('exp_stat', models.IntegerField(default=0)),
                ('total_exp', models.IntegerField(default=0)),
                ('title_color', models.IntegerField(default=0)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.title')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
