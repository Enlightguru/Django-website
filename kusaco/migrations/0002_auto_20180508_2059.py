# Generated by Django 2.0.4 on 2018-05-08 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kusaco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_by', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('capacity', models.CharField(max_length=30)),
                ('year_joined', models.DateField()),
                ('year_graduated', models.DateField()),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone', models.IntegerField(blank=True)),
                ('testimonial', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
