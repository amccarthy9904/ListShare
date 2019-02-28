from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import List

def home(request):
    lists = List.objects.all()
    return render(request, 'home.html', {'lists':lists})
    #return HttpResponse('<p>home view</p>')

def list_detail(request, id):
    try:
        lists = List.objects.get(id=id)
    except List.DoesNotExist:
        raise Http404('List not found')
    return render(request, 'list_detail.html', {'list':list})
    #return HttpResponse('<p>list_detail view wioth id {}</p>'.format(id))
