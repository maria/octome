# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        fields = (
            ('id', models.AutoField(primary_key=True)),
            ('school', models.CharField(max_length=80)),
            ('degree', models.CharField(max_length=60)),
            ('field', models.CharField(max_length=60)),
            ('city', models.CharField(max_length=60)),
            ('country', models.CharField(max_length=60)),
            ('start_date', models.DateField()),
            ('end_date', models.DateField(null=True)),
            ('description', models.TextField()),
            ('url', models.URLField(null=True)),
            ('image', models.ImageField(upload_to='images', null=True, blank=True))
        )
        db.create_table('octo_cv_education', fields)
        db.send_create_signal('octo_cv', ['Education'])

    def backwards(self, orm):
        db.delete_table('octo_cv_education')

    models = {}

    complete_apps = ['octo_cv']
