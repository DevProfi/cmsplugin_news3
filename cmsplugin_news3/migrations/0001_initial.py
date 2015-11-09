# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.db.models.deletion
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNews3',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('limit', models.PositiveIntegerField(default=3, help_text='Limits the number of items that will be displayed', verbose_name='Numbers of news items to show')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='News3',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(help_text='A slug is a short name which uniquely identifies the news item for this day', verbose_name='Slug', unique_for_date=b'pub_date')),
                ('excerpt', models.TextField(verbose_name='Excerpt', blank=True)),
                ('content', models.TextField(verbose_name='Content', blank=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='Published')),
                ('pub_date', models.DateField(default=datetime.datetime(2015, 11, 9, 15, 26, 21, 236589), verbose_name='Publication date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('photo', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='filer.Image', help_text='Optional. Image for news article.', null=True)),
            ],
            options={
                'ordering': ('-pub_date',),
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'permissions': (('can_publish', 'Can publish/unpublish news article'),),
            },
            bases=('cms.cmsplugin',),
        ),
    ]
