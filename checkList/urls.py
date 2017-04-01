from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.check_list,name="check_list"),
]