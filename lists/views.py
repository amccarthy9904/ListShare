from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import List

# TODO: refactor these to use sessions when users are a real thing
#https://docs.djangoproject.com/en/2.1/topics/http/sessions/
def home(request):
    lists = List.objects.all()
    return render(request, 'home.html', {'lists':lists})
    #return HttpResponse('<p>home view</p>')

def list_detail(request, id):
    try:
        list = List.objects.get(id=id)
    except List.DoesNotExist:
        raise Http404('List not found')
    return render(request, 'list_detail.html', {'list':list}, {'id':id})
    #return HttpResponse('<p>list_detail view wioth id {}</p>'.format(id))
