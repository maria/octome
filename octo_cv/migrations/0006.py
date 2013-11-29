# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        fields = (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=30)),
            ('description', models.TextField()),
            ('url', models.URLField(null=True)),
            ('type', models.CharField(max_length=30)),
        )
        db.create_table('octo_cv_project', fields)
        db.send_create_signal('octo_cv', ['Project'])

    def backwards(self, orm):
        db.delete_table('octo_cv_project')

    models = {}

    complete_apps = ['octo_cv']
