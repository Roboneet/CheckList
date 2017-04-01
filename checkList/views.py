from django.shortcuts import render

# Create your views here.

def check_list(request):
	return render(request,'checkList/index.html',{})