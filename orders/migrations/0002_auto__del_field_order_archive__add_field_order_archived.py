# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Order.archive'
        db.delete_column('orders_order', 'archive')

        # Adding field 'Order.archived'
        db.add_column('orders_order', 'archived',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Order.archive'
        db.add_column('orders_order', 'archive',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Order.archived'
        db.delete_column('orders_order', 'archived')


    models = {
        'orders.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'orders.item': {
            'Meta': {'object_name': 'Item'},
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Order']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'orders.order': {
            'Meta': {'object_name': 'Order'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 3, 11, 0, 0)'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 3, 11, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['orders']