# Generated by Django 4.1.5 on 2023-04-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_likepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]