# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.delete_column('octo_cv_project', 'type')


    def backwards(self, orm):
         db.add_column('octo_cv_project', 'type')


    models = {}

    complete_apps = ['octo_cv']
