from django.conf.urls import url, patterns
from django.contrib import admin

from orders.views import OrderView

admin.autodiscover()

urlpatterns = patterns('',
       url(r'^$', OrderView.as_view()),
    )
