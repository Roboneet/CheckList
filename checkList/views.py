from django.shortcuts import render, get_object_or_404
from .models import Item
# Create your views here.

def index(request):
	items = Item.objects.all()
	return render(request,'checkList/main.html',{'items':items})


def item_detail(request,pk):
	item = get_object_or_404(Item,pk=pk)
	return render(request,'checklist/item_details.html',{'item': item})