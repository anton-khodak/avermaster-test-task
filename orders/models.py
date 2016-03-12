# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import Sum
from django.utils import timezone


class Customer(models.Model):
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=10)
    name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField(verbose_name='Фамилия', max_length=30)
    address = models.CharField(verbose_name='Адрес', max_length=100)

    def __unicode__(self):
        return self.name + ' ' + self.surname


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    date_created = models.DateTimeField(default=timezone.now())
    date_edited = models.DateTimeField(default=timezone.now())
    total_cost = models.IntegerField(null=True)
    archived = models.BooleanField(default=False)

    def update_total_cost(self):
        self.total_cost = Item.objects.filter(order=self.pk).aggregate(Sum('cost'))['cost__sum']

    def save(self, *args, **kwargs):
        self.update_total_cost()
        return super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.customer.__unicode__() + ' / ' + str(self.date_created) + ' / ' + str(self.total_cost)


class Item(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    cost = models.FloatField(verbose_name='Цена',)
    quantity = models.IntegerField(verbose_name='Количество',)
    order = models.ForeignKey(Order, verbose_name='Заказ', blank=True)

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)
        self.order.date_edited = timezone.now()
        self.order.save()

    def __unicode__(self):
        return self.name + ' / ' + str(self.cost) + ' / ' + str(self.quantity)
