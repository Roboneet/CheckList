from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^item/(?P<pk>\d+)$',views.item_detail, name="item_detail"),
]