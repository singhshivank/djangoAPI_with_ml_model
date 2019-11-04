# Generated by Django 2.2.5 on 2019-10-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('email', models.EmailField(help_text='Required. Inform a valid email address.', max_length=254)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]