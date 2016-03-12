from django import forms
from django.forms.models import inlineformset_factory

from orders.models import Customer, Item, Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer


class ItemForm(forms.ModelForm):
    def __init__(self, *arg, **kwarg):
        super(ItemForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False  # at least one item must be ordered

    class Meta:
        exclude = ('order',)
        model = Item


ItemFormset = inlineformset_factory(Order, Item, form=ItemForm, extra=1)
