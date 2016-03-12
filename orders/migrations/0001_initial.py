# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table('orders_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('orders', ['Customer'])

        # Adding model 'Order'
        db.create_table('orders_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Customer'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 3, 11, 0, 0))),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 3, 11, 0, 0))),
            ('total_cost', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('archive', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('orders', ['Order'])

        # Adding model 'Item'
        db.create_table('orders_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cost', self.gf('django.db.models.fields.FloatField')()),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Order'])),
        ))
        db.send_create_signal('orders', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table('orders_customer')

        # Deleting model 'Order'
        db.delete_table('orders_order')

        # Deleting model 'Item'
        db.delete_table('orders_item')


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
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Customer']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 3, 11, 0, 0)'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 3, 11, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['orders']