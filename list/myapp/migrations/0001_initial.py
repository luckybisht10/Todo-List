# Generated by Django 4.2 on 2023-05-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('complete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
