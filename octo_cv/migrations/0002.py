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
            ('url', models.URLField(null=True)),
            ('image', models.ImageField(null=True)),
            ('email', models.EmailField(null=True)),
        )
        db.create_table('octo_cv_contact', fields)

    def backwards(self, orm):
        db.delete_table('octo_cv_contact')

    models = {}

    complete_apps = ['octo_cv']
