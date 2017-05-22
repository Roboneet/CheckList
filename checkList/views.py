from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
# Create your views here.

def index(request):
	ticked_items = Item.objects.filter(tick=True)
	unticked_items = Item.objects.filter(tick=False)
	return render(request,'checkList/main.html',{'ticked':ticked_items,'unticked':unticked_items})


def item_detail(request,pk):
	item = get_object_or_404(Item,pk=pk)
	print "in detail view"
	print item.tick
	return render(request,'checkList/item_details.html',{'item': item})

def item_new(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.author = request.user
			item.save()
			return redirect('item_detail',item.pk)
	else:
		form = ItemForm()
	return render(request,'checkList/item_new.html',{'form':form})

def item_tick(request, pk):
	print "asb"
	item = get_object_or_404(Item, pk=pk)
	item.put_tick()
	print item.tick
	return redirect('item_detail',item.pk)


def item_delete(request,pk):
	item = get_object_or_404(Item, pk=pk)
	item.delete()
	return redirect('index')