# Generated by Django 2.0 on 2017-05-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('pub_data', models.DateField()),
            ],
        ),
    ]
