# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160810_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('awarder', models.CharField(max_length=100)),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursecode', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=100)),
                ('studytype', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('gpa', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InterestKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Interest')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('level', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('LI', 'Linkedin')], max_length=2)),
                ('username', models.CharField(max_length=150)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('publisher', models.CharField(max_length=150)),
                ('releaseDate', models.DateField()),
                ('website', models.URLField()),
                ('summary', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('reference', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
                ('picture', models.URLField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=14)),
                ('website', models.URLField()),
                ('summary', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('postalcode', models.CharField(max_length=9)),
                ('city', models.CharField(max_length=255)),
                ('countrycode', models.CharField(max_length=2)),
                ('region', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SkillKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volunteer', models.BooleanField()),
                ('company', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('website', models.URLField()),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('summary', models.TextField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='WorkHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.TextField()),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Work')),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='description',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='image',
        ),
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.CharField(default='none', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AddField(
            model_name='skillkeyword',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Skill'),
        ),
        migrations.AddField(
            model_name='reference',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Resume'),
        ),
        migrations.AddField(
            model_name='publication',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Resume'),
        ),
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Resume'),
        ),
        migrations.AddField(
            model_name='language',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Resume'),
        ),
        migrations.AddField(
            model_name='interestkeyword',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Keyword'),
        ),
        migrations.AddField(
            model_name='interest',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Resume'),
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Resume'),
        ),
        migrations.AddField(
            model_name='course',
            name='education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Education'),
        ),
        migrations.AddField(
            model_name='award',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Resume'),
        ),
        migrations.AddField(
            model_name='skill',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Resume'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='skillkeyword',
            unique_together=set([('skill', 'keyword')]),
        ),
        migrations.AlterUniqueTogether(
            name='interestkeyword',
            unique_together=set([('interest', 'keyword')]),
        ),
    ]
