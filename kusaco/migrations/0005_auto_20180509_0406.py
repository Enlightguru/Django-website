# Generated by Django 2.0.4 on 2018-05-09 01:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kusaco', '0004_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('day', models.CharField(max_length=50)),
                ('time_start', models.TimeField(default=django.utils.timezone.now)),
                ('time_end', models.TimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='albumimage',
            name='album',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='AlbumImage',
        ),
    ]
