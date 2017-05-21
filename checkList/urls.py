from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^item/(?P<pk>\d+)$',views.item_detail, name="item_detail"),
	url(r'^item/new$',views.item_new, name="item_new"),
	url(r'^item/tick/(?P<pk>\d+)$',views.item_tick, name="item_tick"),
]