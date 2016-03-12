from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from orders.forms import ItemFormset, CustomerForm
from orders.models import Order, Item


class OrderView(CreateView):
    template_name = "order.html"
    form_class = CustomerForm

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ItemFormset(self.request.POST)
        else:
            context['formset'] = ItemFormset(queryset=Item.objects.none(),)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()  # saving customer
            order = Order(customer=self.object)
            order.save()  # creating order
            formset.instance = order
            formset.save()  # saving items
            order.save()  # updating total price
            return HttpResponseRedirect('/admin/orders/order/')
        else:
            return self.render_to_response(self.get_context_data(form=form))
