# Generated by Django 3.2.7 on 2021-09-12 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='updated_at',
            new_name='modified_at',
        ),
    ]
