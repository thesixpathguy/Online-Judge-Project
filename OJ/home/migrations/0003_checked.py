# Generated by Django 3.2.4 on 2021-07-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210711_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('code', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]