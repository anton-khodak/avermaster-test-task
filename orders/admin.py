# -*- coding: utf-8 -*-

from daterange_filter.filter import DateRangeFilter
from django.contrib import admin

from orders.models import Customer, Item, Order


class ItemInline(admin.TabularInline):
    model = Item


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['total_cost']
    list_filter = [('date_created', DateRangeFilter), 'archived']
    list_display = ['date_created', 'date_edited', 'phone', 'customer_name', 'total_cost', 'items', 'archived']
    inlines = [
        ItemInline,
    ]
    list_per_page = 20

    def phone(self, obj):
        return "+7(%s)%s" % (str(obj.customer.phone_number[:3]), str(obj.customer.phone_number[3:]))

    def customer_name(self, obj):
        return "%s %s" % (obj.customer.surname.encode('utf-8'), obj.customer.name.encode('utf-8'))

    customer_name.admin_order_field = 'customer__surname'

    def address(self, obj):
        return str(obj.customer.address)

    def phone_number(self, obj):
        return obj.customer.phone_number

    def items(self, obj):
        return '<br/>'.join('<a href="/admin/orders/item/%i/" target="_blank"> %s </a> <br/>' % (item.id, item.name)
                            for item in Item.objects.filter(order=obj.pk))

    items.allow_tags = True

    def save_formset(self, request, form, formset, change):
        # items must be saved before order in order to count total cost correctly
        formset.save()
        form.instance.save()

    class Media:
        js = ('js/jquery-2.2.1.min.js',
              'js/own.js',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Customer)
admin.site.register(Item)
