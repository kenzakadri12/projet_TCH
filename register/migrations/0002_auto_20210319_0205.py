# Generated by Django 3.1.7 on 2021-03-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='Password',
            new_name='password',
        ),
        migrations.AddField(
            model_name='signup',
            name='name',
            field=models.CharField(default='Some name', max_length=122),
        ),
    ]
