# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('orders_order', 'total_price', 'total_cost')

    def backwards(self, orm):
        db.rename_column('orders_order',  'total_cost', 'total_price',)


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
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Order']", 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'orders.order': {
            'Meta': {'object_name': 'Order'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 3, 12, 0, 0)'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 3, 12, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['orders']