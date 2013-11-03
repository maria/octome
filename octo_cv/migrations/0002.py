# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        fields = (
            ('id', models.AutoField(primary_key=True)),
            ('type', models.CharField(max_length=20)),
            ('name', models.CharField(max_length=30)),
            ('description', models.TextField()),
            ('url', models.URLField(null=True, blank=True)),
            ('image', models.ImageField(upload_to='images', null=True, blank=True)),
            ('email', models.EmailField(null=True, blank=True)),
        )
        db.create_table('octo_cv_contact', fields)
        db.send_create_signal('octo_cv', ['Contact'])

    def backwards(self, orm):
        db.delete_table('octo_cv_contact')

    models = {}

    complete_apps = ['octo_cv']
