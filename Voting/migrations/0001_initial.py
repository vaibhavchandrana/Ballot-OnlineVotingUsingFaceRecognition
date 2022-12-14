# Generated by Django 4.1.1 on 2022-09-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=500)),
                ('voter_id', models.IntegerField()),
                ('profile', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
