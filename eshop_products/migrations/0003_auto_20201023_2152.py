# Generated by Django 3.1.2 on 2020-10-23 18:22

from django.db import migrations, models
import eshop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0002_auto_20201018_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False, verbose_name='فعال/غیرفعال'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=eshop_products.models.upload_image_path, verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=150, verbose_name='عنوان'),
        ),
    ]
