# Generated by Django 4.2.11 on 2024-11-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='item',
            name='email',
            field=models.EmailField(default='0000000000', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='items/'),
        ),
        migrations.AddField(
            model_name='item',
            name='phone',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='item',
            name='second_name',
            field=models.CharField(default='0000000000', max_length=20),
        ),
    ]