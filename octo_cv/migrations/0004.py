# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        fields = (
            ('id', models.AutoField(primary_key=True)),
            ('type', models.CharField(max_length=30)),
            ('company', models.CharField(max_length=80)),
            ('role', models.CharField(max_length=80)),
            ('city', models.CharField(max_length=60)),
            ('country', models.CharField(max_length=60)),
            ('description', models.TextField()),
            ('url', models.URLField(null=True)),
            ('start_date', models.DateField()),
            ('end_date', models.DateField(null=True)),
        )
        db.create_table('octo_cv_work', fields)
        db.send_create_signal('octo_cv', ['Work'])

    def backwards(self, orm):
        db.delete_table('octo_cv_work')

    models = {}

    complete_apps = ['octo_cv']
