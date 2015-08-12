# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'State.abbreviation'
        db.alter_column(u'main_state', 'abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'State.name'
        db.alter_column(u'main_state', 'name', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True, null=True))
        # Adding field 'StateCapital.state'
        db.add_column(u'main_statecapital', 'state',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.State'], unique=True, null=True),
                      keep_default=False)


        # Changing field 'StateCapital.latitude'
        db.alter_column(u'main_statecapital', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StateCapital.longitutde'
        db.alter_column(u'main_statecapital', 'longitutde', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StateCapital.population'
        db.alter_column(u'main_statecapital', 'population', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'State.abbreviation'
        db.alter_column(u'main_state', 'abbreviation', self.gf('django.db.models.fields.CharField')(default=1, max_length=2))

        # Changing field 'State.name'
        db.alter_column(u'main_state', 'name', self.gf('django.db.models.fields.CharField')(default=1, max_length=30, unique=True))
        # Deleting field 'StateCapital.state'
        db.delete_column(u'main_statecapital', 'state_id')


        # Changing field 'StateCapital.latitude'
        db.alter_column(u'main_statecapital', 'latitude', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'StateCapital.longitutde'
        db.alter_column(u'main_statecapital', 'longitutde', self.gf('django.db.models.fields.FloatField')(default=1))

        # Changing field 'StateCapital.population'
        db.alter_column(u'main_statecapital', 'population', self.gf('django.db.models.fields.IntegerField')(default=1))

    models = {
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True', 'null': 'True'})
        },
        u'main.statecapital': {
            'Meta': {'object_name': 'StateCapital'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitutde': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.State']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['main']