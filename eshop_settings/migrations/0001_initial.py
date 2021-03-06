# Generated by Django 3.1.2 on 2020-11-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان سایت')),
                ('address', models.CharField(max_length=400, verbose_name='آدرس')),
                ('phone', models.CharField(max_length=50, verbose_name='تلفن')),
                ('mobile', models.CharField(max_length=50, verbose_name='موبایل')),
                ('fax', models.CharField(max_length=50, verbose_name='فکس')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'مدیریت تنظیمات',
            },
        ),
    ]
