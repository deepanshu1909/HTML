# Generated by Django 4.1.1 on 2022-10-12 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gupms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Makeinfo',
        ),
    ]
